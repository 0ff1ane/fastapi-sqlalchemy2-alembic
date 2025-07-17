interface ITodo {
  id: number;
  content: string;
  is_completed: boolean;
  is_deleted: boolean;
  created_at: string;
  updated_at: string;
}

async function addTodoFn(content: string): Promise<ITodo> {
  const resp = await fetch("/api/todos", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content }),
  });
  return await resp.json();
}

async function updateTodoFn(
  id: number,
  is_completed: boolean,
  is_deleted: boolean,
): Promise<ITodo> {
  const resp = await fetch(`/api/todos/${id}`, {
    method: "PUT",
    headers: {
      accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ is_completed, is_deleted }),
  });
  return await resp.json();
}

async function getTodosFn(): Promise<{ count: number; items: ITodo[] }> {
  const resp = await fetch("/api/todos", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  return await resp.json();
}

export { addTodoFn, updateTodoFn, getTodosFn };
