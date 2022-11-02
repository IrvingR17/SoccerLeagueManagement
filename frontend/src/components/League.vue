<template>
    <div class="containe">
        <div class="info">
            <h2></h2>
        </div>
    </div>
</template>
<script>
export default {
    name: 'League',

    data() {
        return {

        }
    }
}
</script>
<style scoped>
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }
    .containe {
        display: flex;
    }
    .info {
        flex: 80%;
    }
    h2 {
        border-bottom: 1px solid black;
        text-align: left;
        margin: 0 15px 0 15px;
    }
</style>