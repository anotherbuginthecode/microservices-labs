<template>
  <TheNavbar />
  <section class="w-full mt-10 flex justify-center">
    <div class="w-1/2 flex justify-center items-center">
      <div class="w-full">
        <h1 class="font-bold text-2xl text-center mb-5 text-neutral-900">TODO</h1>
        <div class="flex justify-center gap-x-5">
          <input
            v-model="newTask"
            type="text"
            class=" form-control block w-1/2 px-4 py-2 text-xl font-normal text-neutral-900 bg-white bg-clip-padding
              border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-neutral-900 focus:bg-white focus:outline-none"
          />
          <button 
            @click="addTask()"
            class="border rounded px-8 py-2 text-xl bg-green-300 hover:bg-green-500 text-white">
            + Add
          </button>
        </div>

        <!-- new task -->
        <TaskList 
        @onEmitCompleted="markAsCompleted"
        @onEmitDelete="deleteTask"
        :list="todolist" />

        <div v-show="todolistCompleted.length > 0" class="w-1/3 border border-solid border-neutral-900 h-0.5 m-auto mb-5"></div>

        <!-- completed task -->
        <TaskList 
        @onEmitDelete="deleteTask"
        :list="todolistCompleted" />

      </div>

    </div>
  </section>
</template>

<script>
import TaskList from '../components/Tasks/TaskList.vue'
import TheNavbar from '../components/TheNavbar.vue';

import { TODO_API } from '@/api/todo/http-common';

export default {
    name: "Home",
    emits: ["onEmitCompleted"],
    components: { TaskList, TheNavbar },
    data() {
        return {
            newTask: "",
            todolist: [
                {
                    "id": 1,
                    "text": "Go to supermarket",
                    "completed": false
                },
                {
                    "id": 2,
                    "text": "Write an article",
                    "completed": false
                },
            ],
            todolistCompleted: []
        };
    },
    mounted() {
      TODO_API.get('/api/v1/todo/?completed=false')
      .then(res => {
        this.todolist = res.data.items
      })

      TODO_API.get('/api/v1/todo/?completed=true')
      .then(res => {
        this.todolistCompleted = res.data.items
      })
    },
    methods: {
        addTask: function () {
            const payload = {
                "text": this.newTask,
                "completed": false
            }
            TODO_API.post('/api/v1/todo/', payload)
            .then(res => {
              this.todolist.push(res.data);
            })
            .catch(err => {
              console.log(err)
            })
            this.newTask = "";
        },
        markAsCompleted: function(item){
          // set as completed
          TODO_API.post('/api/v1/todo/'+item.todo_id+'/completed/', {'completed': true})
          .then(res => {
            console.log(res.data)
          })
          .catch(err => {
            console.log(err)
          })
          item.completed = true
          // add to completed list
          this.todolistCompleted.push(item)
          //filter todo list
          this.todolist = this.todolist.filter((elem) => {
            return elem.todo_id != item.todo_id
          })
        },
        deleteTask: function(item){
          
          TODO_API.delete('/api/v1/todo/'+item.todo_id+'/')
          .then(res => {
            console.log(res.data)
          })
          .catch(err => {
            console.log(err)
          })

          this.todolist = this.todolist.filter((elem) => {
            return elem.todo_id != item.todo_id
          })

          this.todolistCompleted = this.todolistCompleted.filter((elem) => {
            return elem.todo_id != item.todo_id
          })
        }
    }
}
</script>
