<script lang="ts">
	import { onMount } from "svelte";
    import { swipe } from 'svelte-gestures';
    import "$lib/components/Demo.svelte";
    import lily from "$lib/animations/audio_wavelength.mp4";
	import { goto } from "$app/navigation";


    // Fetch demo songs
    let demoSongId = [
        1906328537,
        803968452,
        72160317
    ]
    let info:any = $state([]);

    function demo_fetch() {
        demoSongId.forEach((id) => {
            fetch(`http://localhost:8000/api/track/${id}`)
                .then((response) => response.json())
                .then((data) => {
                    console.log(data)
                    info = [...info, data]
                })
        })
    }

    // decrement demo_count
    let demo_count = $state(3);
    let audioElement: HTMLAudioElement | null = null;
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
            decrement();
        } else if (direction === 'left') {
            dislikeActive = true;
            likeActive = false;
            decrement();
        }

        // Réinitialiser après un délai pour donner l'effet de relâchement
        setTimeout(() => {
            likeActive = false;
            dislikeActive = false;
        }, 300);
    }

    $effect(() => {
        if (demo_count === 0) {
            goto('/front/auth/login');
        }
    })

    function decrement() {
        demo_count--;
        let tmp = info[0];
        info = info.slice(1);
        info.push(tmp);

        if (audioElement) {
            audioElement.load();
        }
    }

    function swapAudio() {
        if (audioElement) {
            if (isPlaying) {
                audioElement.pause();
            } else {
                audioElement.play();
            }
            isPlaying = !isPlaying;
        }
    }

    onMount(() => {
        demo_fetch()
    })                
</script>



<div use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: 'pan-y' }} onswipe={handler} class="flex flex-col items-center justify-center my-6">
    <div class="stack">
        {#each info as song}
            <img src={song.album.cover_medium} alt={song.title} class="rounded-lg" />
        {/each}
    </div>
    
    <div>
        <video class= "h-16 my-4" autoplay loop>
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
        <button class="btn btn-outline btn-error mr-8 ml-6 {dislikeActive ? 'btn-active' : ''}" aria-label="dislike" onclick={decrement}>
            <i class="fi fi-rr-cross" id="Dislike"></i></button>
        <button class="btn btn-outline btn-success mr-6 ml-8 {likeActive ? 'btn-active' : ''}" aria-label="like" onclick={decrement}>
            <i class="fi fi-rr-heart" id="Like"></i></button>
    </div>
    

</div>
