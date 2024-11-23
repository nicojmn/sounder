<script lang="ts">
	import Demo from "$lib/components/Demo.svelte";
    
    let demo: boolean = true;
</script>

{#if demo}
    <Demo />
{/if}

