<script>
    import { location, push } from "svelte-spa-router";
    import axios from "axios";

    const logout = () => {
        axios.get("/auth/logout")
            .then(res => {
                push("/login");
            });
    };
</script>

<nav class="text-xl bg-gray-900 font-bold flex sticky top-0 z-50">
<div class="w-full text-gray-400 flex">
    <div class="p-2 hover:text-white cursor-pointer" class:current_page={$location === "/"} on:click={() => push("/")}>Page 1</div>
    <div class="p-2 hover:text-white cursor-pointer" class:current_page={$location === "/page2"} on:click={() => push("/page2")}>Page 2</div>
</div>
<div class="">
    <div class="p-2 text-white cursor-pointer" on:click={logout}>logout</div>
</div>
</nav>

<style>
div.current_page {
    @apply text-white;
}
</style>