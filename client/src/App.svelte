<script>
  import svelteLogo from './assets/svelte.svg'
  import Counter from './lib/Counter.svelte'
  import Router from 'svelte-spa-router'
  import { routes } from './router'
</script>

<main>
  <Router {routes} />
</main>

<style>
</style>
