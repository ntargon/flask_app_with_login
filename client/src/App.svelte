<script lang='typescript'>
  import Router, { push, replace } from 'svelte-spa-router'
  import Header from './lib/Header.svelte';
  import Sidebar from './lib/Sidebar.svelte';
  import { routes } from './router'

  const conditionsFailed = (event) => {
    replace("/login");
  }
</script>


<main>
  <div class="sticky top-0 z-50">
    <Header />
  </div>
  <Sidebar />
  <div class="pl-40">
    <Router
      {routes}
      on:conditionsFailed={conditionsFailed}
    />
  </div>
</main>

<style>
</style>
