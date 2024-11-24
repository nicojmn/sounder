<script lang="ts">
	import Demo from "$lib/components/Demo.svelte";
	import { onMount } from "svelte";
    import { swipe } from 'svelte-gestures';
    import "$lib/components/Demo.svelte";
    import lily from "$lib/animations/audio_wavelength.mp4";
	import { goto } from "$app/navigation";
    
    let demo: boolean = false;

    let info:any = $state([]);
    let songBatch = $state(3);

    let audioElement: HTMLAudioElement | null = null;
    let lilyElement: HTMLVideoElement | null = null;
    let isPlaying = $state(true);
    // Swipe handler
    let direction;
    let likeActive = $state(false);
    let dislikeActive = $state(false);
  
    function handler(event: any) {
      direction = event.detail.direction;

        // Activer les styles selon la direction du swipe
        if (direction === 'right') {
            likeActive = true;
            dislikeActive = false;
            next_song(true);
        } else if (direction === 'left') {
            dislikeActive = true;
            likeActive = false;
            next_song(false);
        }

        // Réinitialiser après un délai pour donner l'effet de relâchement
        setTimeout(() => {
            likeActive = false;
            dislikeActive = false;
        }, 300);
    }

    function next_song(save: boolean = false) {
        songBatch--;
        let song_to_add = info[0];
        info = info.slice(1);
        
        if (songBatch > 1) {
            getTracks().then(data => {
                data.forEach((track: any) => {
                    getTrackDeezer(track.id)
                }
            )});
            songBatch = 3;
        }
        
        if (audioElement) {
            audioElement.load();
        }

        if (save) {
            fetch(
                `http://localhost:8000/api/playlist/add/${song_to_add.spotify_id}`,
                {
                    method: "POST"
                }
            )
        }         
    }

    function swapAudio() {
        if (audioElement) {
            if (isPlaying) {
                audioElement.pause();
                if (lilyElement) {
                    lilyElement.pause();
                }
            } else {
                audioElement.play();
                if (lilyElement) {
                    lilyElement.play();
                }
            }
            isPlaying = !isPlaying;
        }
    }
    
    function userIsAuthenticated() { // auth to spotify
        fetch("http://localhost:8000/api/user_is_auth")
            .then(res => res.json())
            .then(data => {
                if (data.is_auth) {
                    return true;
                }
                return false;
            })
        return false;
    }

    async function getTracks() {
        let response = await fetch("http://localhost:8000/api/recommendations")
        let data = await response.json()
        return data
    }

    function getTrackDeezer(id: string) {
        fetch(`http://localhost:8000/api/song_deezer/${id}`)
            .then(res => res.json())
            .then(data => {
                data.spotify_id = id
                info = [...info, data]
            })
    }

    onMount(() => {
        console.log("onMount");
        getTracks().then(data => {
            data.forEach((track: any) => {
                getTrackDeezer(track.id)
            }
        )});
    });
</script>

{#if demo}
    <Demo />
{:else}
    <div use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: 'pan-y' }} onswipe={handler} class="flex flex-col items-center justify-center my-6">
        <div class="stack">
            {#each info as song}
                <img src={song.album.cover_medium} alt={song.title} class="rounded-lg" />
            {/each}
        </div>
        
        <div>
            <video class= "h-16 my-4" autoplay loop bind:this={lilyElement}>
                <track kind="captions" />
                <source src={lily} type="video/mp4">
            </video>
        </div>

        
        <div>
            <audio autoplay loop bind:this={audioElement}>
                {#each info as song}
                    <source src={song.preview} type="audio/mpeg">
                {/each}
            </audio>
            <button class="btn btn-circle" aria-label="play" onclick={swapAudio}>
                {#if isPlaying}
                    <i class="fi fi-rr-pause"></i>
                {:else}
                    <i class="fi fi-rr-play"></i>
                {/if}
            </button>
        </div>

        <div class="my-5 space-x-36">
            <button class="btn btn-outline btn-error mr-8 ml-6 {dislikeActive ? 'btn-active' : ''}" aria-label="dislike" onclick={() => next_song(false)}>
                <i class="fi fi-rr-cross" id="Dislike"></i></button>
            <button class="btn btn-outline btn-success mr-6 ml-8 {likeActive ? 'btn-active' : ''}" aria-label="like" onclick={() => next_song(true)}>
                <i class="fi fi-rr-heart" id="Like"></i></button>
        </div>
    </div>
{/if}

