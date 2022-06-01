<template>
    <div id="todolistContainerNew" class="mt-10">
        <Task 
            @completed="handleCompleted" 
            @delete="handleDelete"
            v-for="item in list" :key="item.id" :item="item"/>
    </div>
</template>

<script>
import Task from './Task'

export default {
    name: 'TaskList',
    props: {
        list: { type: Array, default: () => []}
    },
    components: {
        Task
    },
    emits: ['completed', 'onEmitCompleted', 'delete', 'onEmitDelete'],
    methods: {
        handleCompleted: function(item){
            // api call to set completed as true


            this.$emit('onEmitCompleted', item)
        },
        handleDelete: function(item){
            // api call to delete record
            this.$emit('onEmitDelete', item)
        }
    }
}
</script>

<style>

</style>