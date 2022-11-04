<template>
    <div class="containe">
        <div class="info">
            <h2>{{league_info.name}}</h2>
            <div class="content">

                    <b-button variant="primary">Agregar equipo</b-button>
                    <b-button variant="warning">Editar liga</b-button>

                    <b-table :items="teams" :fields="fields" caption-top>
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
                {key: 'goals_against', label: 'GF'},
                {key: 'score', label: 'Puntos'},
            ]
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