<script lang="ts">
	import '$lib/app.css';

	let demo: boolean = true;
</script>


{#if !demo}
	<div role="alert" class="alert alert-warning">
		<span>🚧 This webapp is under construction</span>
	</div>
{/if}

<div class="navbar bg-base-100">
	<div class="flex-1 justify-center">
		<a class="btn btn-ghost text-xl">Sounder</a>
	</div>
</div>
