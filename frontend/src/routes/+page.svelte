<script lang="ts">
    import { goto } from "$app/navigation";
    import { swipe } from 'svelte-gestures';
    import deezer_logo from "$lib/assets/images/deezer.svg";
    import "$lib/components/CoverStack.svelte";
	import CoverStack from "$lib/components/CoverStack.svelte";
    
    let demo: boolean = true;

    let direction;
    let likeActive = false;
    let dislikeActive = false;
  
    function handler(event: any) {
      direction = event.detail.direction;

        // Activer les styles selon la direction du swipe
        if (direction === 'right') {
            likeActive = true;
            dislikeActive = false;
        } else if (direction === 'left') {
            dislikeActive = true;
            likeActive = false;
        }

        // Réinitialiser après un délai pour donner l'effet de relâchement
        setTimeout(() => {
            likeActive = false;
            dislikeActive = false;
        }, 300);
    }
</script>



<div use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: 'pan-y' }} on:swipe={handler} class="justify-items-center" id="Box-Music">
    <CoverStack {demo}/>     

    <div class="place-items-center my-5" id="Name">
        <h1>
            Auteur
        </h1>
    </div>

    <div class="justify-items-center my-5"  id="Sound">
        <audio controls id="audio">
            <source src="ocean-waves-112906.mp3" type="audio/mpeg">
        </audio>
    </div>

      <div class="justify-items-center my-5 space-x-36" id="Choice">
        <button class="btn btn-outline btn-error mr-8 ml-6 {dislikeActive ? 'btn-active' : ''}"><i class="fi fi-rr-cross" id="Dislike"></i></button>
        <button class="btn btn-outline btn-success mr-6 ml-8 {likeActive ? 'btn-active' : ''}"><i class="fi fi-rr-heart" id="Like"></i></button>
    </div>
    

</div>
