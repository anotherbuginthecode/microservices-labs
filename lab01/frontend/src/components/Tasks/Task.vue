<template>
    <div
        class="border rounded border-solid border-gray-300 px-4 py-4 text-neutral-900 bg-white shadow-xl w-2/3 flex justify-between mb-5 m-auto"
        :class="[item.completed ? 'line-through' : '']"
        >
        <p>{{item.text}}</p>
        <div class="flex justify-around gap-x-5">
            <svg
            v-show="item.completed === false" 
            @click="emitCompleted" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-300 cursor-pointer" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            <svg @click="emitDelete" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 cursor-pointer" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        item: {  type: Object, default: () => {} }
    },
    methods: {
        emitCompleted: function(){
            this.$emit('completed', this.item)
        },
        emitDelete: function(){
            this.$emit('delete', this.item)
        }
    }

}
</script>

<style>

</style>