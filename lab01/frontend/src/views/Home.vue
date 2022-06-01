<template>
  <div class="w-full h-screen flex justify-center">
    <div class="w-1/2 flex justify-center items-center">
      <div class="w-full">
        <h1 class="font-bold text-2xl text-center mb-5 text-neutral-900">TODO List</h1>
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
        <!-- list -->
        <div id="todolistContainerNew" class="mt-10">
          <div
            v-for="(item,index) in todolist" :key="item.id"
            class="border rounded border-solid border-gray-300 px-4 py-4 text-neutral-900 bg-white shadow-xl w-2/3 flex justify-between mb-5 m-auto"
            :class="[item.completed ? 'line-through' : '']"
            >
            <p>{{item.text}}</p>
            <div class="flex justify-around gap-x-5">
              <svg
                v-show="item.completed === false" 
                @click="markAsCompleted(index, item)" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-300 cursor-pointer" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <svg @click="deleteTask(index)" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 cursor-pointer" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
            </div>
          </div>
        </div>

        <div class="w-1/3 border border-solid border-neutral-900 h-0.5 m-auto mb-5"></div>

        <div id="todolistContainerCompleted">
          <div
            v-for="(item,index) in todolistCompleted" :key="item.id"
            class="border rounded border-solid border-gray-300 px-4 py-4 text-neutral-900 bg-white shadow-xl w-2/3 flex justify-between mb-5 m-auto"
            :class="[item.completed ? 'line-through' : '']"
            >
            <p>{{item.text}}</p>
            <div class="flex justify-around gap-x-5">
              <svg
                v-show="item.completed === false" 
                @click="markAsCompleted(index)" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-300 cursor-pointer" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <svg @click="deleteTask(index)" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 cursor-pointer" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      newTask: '',
      todolist: [
        {
          'id': 1,
          'text': 'Go to supermarket',
          'completed': false
        },
        {
          'id': 2,
          'text': 'Write an article',
          'completed': false
        },
      ],
      todolistCompleted: [
        {
          'id': 3,
          'text': 'Read 10 pages of a book',
          'completed': true
        }
      ]
    }
  },
  methods: {
    markAsCompleted: function(index, item){
      this.todolist[index].completed = true
      this.todolist.splice(index,1)
      this.todolistCompleted.push(item)
    },
    deleteTask: function(index){
      this.todolist.splice(index,1)
    },
    addTask: function(){
      this.todolist.push({
        'id': 4,
        'text': this.newTask,
        'completed': false
      })
      this.newTask = ''
    }
  }

}
</script>
