<template>
    <div class="containe">
        <div class="info">
            <h2>{{team.name}}</h2>
            <div class="content">

                    <b-table selectable select-mode="single" hover @row-selected="" :items="players" :fields="fields" caption-top>
                        <template #table-caption>Jugadores</template>
                    </b-table>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Team',

    data() {
        return {
            team: '',
            players: [],
            fields: [
                {key: 'player.first_name', label: 'Nombre'},
                {key: 'goals', label: 'Goles'},
            ],  
        }
    },
    methods: {
        async getTeamInfo() {
            this.id = this.$route.params.id
            let path = "http://127.0.0.1:8000/api/teams/list2/" + this.id
            await axios.get(path).then((response) => {
                this.team = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            let path2 = "http://127.0.0.1:8000/api/team_player/list/" + this.id
            await axios.get(path2).then((response) => {
                this.players = response.data
                console.log(this.players)
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getTeamInfo()
    }
}
</script>

<style scoped>
.containe {
    display: flex;
}
.info {
    flex: 80%;
    margin: 15px;
}
h2 {
    border-bottom: 1px solid black;
    text-align: left;
}
</style>