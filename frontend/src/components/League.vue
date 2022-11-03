<template>
    <div class="containe">
        <div class="info">
            <h2>{{league_info.name}}</h2>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'League',

    data() {
        return {
            league_info: null,
            id: null,
        }
    },
    methods: {
        async getLeagueInfo() {
            this.id = this.$route.params.id
            const path = "http://127.0.0.1:8000/api/leagues/list/" + this.id
            await axios.get(path).then((response) => {
                this.league_info = response.data
                console.log(this.league_info)
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getLeagueInfo()
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