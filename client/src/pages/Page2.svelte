<script>
    let data = [
        {
            id: 0,
            name: "hoge2",
            date: "2022/2/2"
        },
        {
            id: 1,
            name: "hoge4",
            date: "2022/4/2"
        },
        {
            id: 2,
            name: "hoge1",
            date: "2022/7/2"
        },
        {
            id: 3,
            name: "hoge11",
            date: "2024/3/2"
        },
    ]

    $: sort = (key) => {
        data = data.sort((a, b) => {
            if ( a[key] < b[key] ) {
                return -1;
            } else if ( a[key] > b[key] ) {
                return 1;
            } else {
                return 0;
            }
        });
    }

    const openWindow = () => {
        window.open("/#/page2");
    }
</script>
<div>
    <div>
        <button on:click={openWindow} class="bg-blue-200 hover:bg-blue-400 border-2 border-gray-600 rounded-md p-2 m-2">open in new tab</button>
    </div>
    <div class="p-4">
        <table class="table-auto w-full text-right">
            <thead>
                <tr class="bg-blue-200">
                    <th>count</th>
                    <th class="hover:bg-blue-300 hover:cursor-pointer" on:click={() => sort("id")}>id</th>
                    <th class="hover:bg-blue-300 hover:cursor-pointer" on:click={() => sort("name")}>name</th>
                    <th class="hover:bg-blue-300 hover:cursor-pointer" on:click={() => sort("date")}>date</th>
                </tr>
            </thead>
            <tbody>
                {#each data as {id, name, date}, i}
                <tr class:bg-blue-50={i % 2 === 1}>
                    <td>{i}</td>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{date}</td>
                </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>

<style>
td, th {
    @apply border px-4 py-2;
}
</style>