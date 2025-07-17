<script lang="ts">
    import { createMutation, createQuery } from "@tanstack/svelte-query";
    import { addTodoFn, getTodosFn, updateTodoFn } from "../queries/todos";

    let props = $props();

    const todosQuery = createQuery({
        queryKey: ["todos"],
        queryFn: getTodosFn,
    });

    const addTodoMutation = createMutation({
        mutationFn: () => addTodoFn(newTodoText),
        onSuccess: (todo) => {
            $todosQuery.refetch();
            newTodoText = "";
        },
    });

    const updateTodoMutation = createMutation({
        mutationFn: ({
            id,
            is_completed,
            is_deleted,
        }: {
            id: number;
            is_completed: boolean;
            is_deleted: boolean;
        }) => updateTodoFn(id, is_completed, is_deleted),
        onSuccess: (todo) => {
            $todosQuery.refetch();
            newTodoText = "";
        },
    });

    let todos = $state([
        { text: "Complete svelte tutorial", complete: true },
        { text: "Build todo app", complete: true },
        { text: "Read TypeScript documentation", complete: false },
        { text: "Write unit tests", complete: false },
        { text: "Deploy to production", complete: false },
    ]);
    let newTodoText = $state("");
    let isValidTodoText = $derived(newTodoText.length > 5);

    function addTodo() {
        $addTodoMutation.mutate();
    }

    function updateTodo(
        id: number,
        is_deleted: boolean,
        is_completed: boolean,
    ) {
        $updateTodoMutation.mutate({ id, is_deleted, is_completed });
    }
</script>

<div class="relative py-12 max-w-md mx-auto">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full flex flex-col gap-4">
        <h1 class="text-2xl text-gray-800 mb-6 text-center">Todo App</h1>

        <div>
            <div class="flex">
                <input
                    type="text"
                    placeholder="Add a new todo"
                    class="flex-grow p-3 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                    disabled={$addTodoMutation.isPending}
                    bind:value={newTodoText}
                    onkeydown={(e) => {
                        if (e.key === "Enter") addTodo();
                    }}
                />
                <button
                    onclick={addTodo}
                    disabled={!isValidTodoText || $addTodoMutation.isPending}
                    class={`bg-gray-600 text-white p-3 rounded-r-lg hover:bg-gray-700 transition-colors duration-200 text-sm ${isValidTodoText ? "cursor-pointer" : "cursor-not-allowed"}`}
                >
                    Add
                </button>
            </div>
            {#if newTodoText.length > 0 && !isValidTodoText}
                <span class="text-red-500 text-xs"
                    >Must be atleast 5 letters long</span
                >
            {/if}
        </div>

        {#if $todosQuery.isLoading}
            <p class="text-gray-500 text-center">
                No todos yet. Add one above!
            </p>
        {:else if $todosQuery.isError}
            <p class="text-gray-500 text-center">
                No todos yet. Add one above!
            </p>
        {:else if $todosQuery.isSuccess}
            {#if $todosQuery.data.count === 0}
                <p class="text-gray-500 text-center">
                    No todos yet. Add one above!
                </p>
            {:else}
                <ul>
                    {#each $todosQuery.data.items as todo, index (todo.id)}
                        <li
                            class="flex items-center justify-between bg-gray-50 p-3 rounded-lg mb-2 shadow-sm"
                        >
                            <input
                                type="checkbox"
                                value={todo.is_completed}
                                disabled={$updateTodoMutation.isPending}
                                onchange={(e) =>
                                    updateTodo(
                                        todo.id,
                                        todo.is_deleted,
                                        e.currentTarget.value === "checked"
                                            ? true
                                            : false,
                                    )}
                                class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded cursor-pointer"
                            />
                            <span
                                class="ml-2 flex-grow text-lg {todo.is_completed
                                    ? 'line-through text-gray-500'
                                    : 'text-gray-800'}"
                            >
                                {todo.content}
                            </span>
                            <button
                                class="ml-4 text-red-500 hover:text-red-700 transition-colors duration-200 text-lg cursor-pointer"
                                disabled={$updateTodoMutation.isPending}
                                onclick={() =>
                                    updateTodo(
                                        todo.id,
                                        !todo.is_deleted,
                                        todo.is_completed,
                                    )}
                            >
                                &#10007;
                            </button>
                        </li>
                    {/each}
                </ul>
            {/if}
        {/if}
    </div>
</div>

<div class="mx-auto max-w-2xl text-center pb-12">
    inertia props = {JSON.stringify(props)}
</div>
