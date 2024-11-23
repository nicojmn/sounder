<script lang="ts">
    import { goto } from "$app/navigation";
    import deezer_logo from "$lib/assets/images/deezer.svg";
    import "$lib/components/CoverStack.svelte";
	import CoverStack from "$lib/components/CoverStack.svelte";
    
    let demo: boolean = true;
</script>


<div class="flex items-center justify-center">
    <CoverStack {demo}/>
    <button class="btn-circle btn-neutral  w-1/5" type="button" on:click={() => {
        goto("/deezer");
    }}>
        <img class="w-full h-full" src={deezer_logo} alt="Deezer logo" />
    </button>
</div>