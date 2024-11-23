<script lang="ts">
	import { onMount } from "svelte";

    let demoSongId = [
        3829144,
        803968452,
        72160317
    ]
    let info: any = []

    function demo_fetch() {
        demoSongId.forEach((id) => {
            fetch(`http://127.0.0.1:8000/api/track/${id}`)
                .then((response) => response.json())
                .then((data) => {
                    info = [...info, data]
                })
        })
    }

    onMount(() => {
        demo_fetch()
    })

    export let demo: boolean;
                
</script>

{#if demo}
    <div class="flex min-w-full items-center">
        <div class="stack">
            {#each info as song}
                <img src={song.album.cover_medium} alt={song.title} class="rounded-lg" />
            {/each}
        </div>
    </div>
{/if}