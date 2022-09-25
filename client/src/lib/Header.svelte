<script>
    import { location } from "svelte-spa-router";
</script>

<nav class="text-xl bg-gray-900 font-bold flex">
<div class="w-full text-gray-400 ">
    <a href="/#/" class="p-4 hover:text-white" class:current_page={$location === "/"}>Page 1</a>
    <a href="/#/page2" class="p-4 hover:text-white" class:current_page={$location === "/page2"}>Page 2</a>
</div>
<div class="">
    <a href="/api/logout" class="p-4 text-white">logout</a>
</div>
</nav>

<style>
a.current_page {
    @apply text-white;
}
</style>