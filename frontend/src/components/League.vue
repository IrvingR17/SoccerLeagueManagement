<template>
    <div class="containe">
        <div class="info">
            <h2>{{league_info.name}}</h2>
            <div class="content">

                    <b-button @click="goToAddTeam()" variant="primary">Agregar equipo</b-button>
                    <b-button @click="goToEdit()" variant="warning">Editar liga</b-button>

                    <b-table selectable select-mode="single" hover @row-selected="goToTeam" :items="teams" :fields="fields" caption-top>
                        <template #table-caption>Tabla de posiciones</template>
                    </b-table>

            </div>
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
            teams: [],
            fields: [
                {key: 'name', label: 'Equipo'},
                {key: 'matches_played', label: 'PJ'},
                {key: 'goals_for', label: 'GF'},
                {key: 'goals_against', label: 'GC'},
                {key: 'score', label: 'Puntos'},
            ],  
            selected: []
        }
    },
    methods: {
        async getLeagueInfo() {
            this.id = this.$route.params.id
            let path = "http://127.0.0.1:8000/api/leagues/list/" + this.id
            await axios.get(path).then((response) => {
                this.league_info = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            path = "http://127.0.0.1:8000/api/teams/list/" + this.id
            await axios.get(path).then((response) => {
                this.teams = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        goToEdit() {
            this.$router.push('/edit_league/' + this.id)
        },
        goToAddTeam() {
            this.$router.push('/add_team/' + this.id)
        },
        goToTeam(teams){
            this.$router.push('/team/' + (this.selected = teams[0].id))

        }
    },
    created() {
        this.getLeagueInfo()
    }
}
</script>
<style scoped>
.containe {
    display: flex;
}
.content {
    margin: 25px 80px 0 80px;
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