<template>
    <div class="containe">
        <div class="info">
            <h2>Menu Ligas</h2>
            <div class="leagues">
                <div class="league-cards">
                    <b-card-group deck>
                        <b-card v-for="league in leagues" 
                            :title="league.name"
                            img-src="https://picsum.photos/600/300/?image=25"
                            img-alt="Image"
                            img-top
                            tag="article"
                            style="max-width: 10rem;"
                            class="league-card"
                        >
                            <b-card-text>
                                {{league.description}}
                            </b-card-text>
        
                            <b-button @click="getId(league.id)" variant="primary">Mas informacion</b-button>
                        </b-card>  
                    </b-card-group>
                </div>
            </div>
            <div class="btn-add-league">
                <b-button @click="$router.push('/register_league')" block variant="primary">Agregar Liga</b-button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Index',
    data() {
        return {
            leagues: null,
        }
    },
    methods: {
        async getCardInfo() {
            const path = 'http://127.0.0.1:8000/api/leagues/list/'
            await axios.get(path).then((response) => {
                this.leagues = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        getId(id){
            this.$router.push('/league/' + id)
        },
    },
    created() {
        this.getCardInfo()
    },
}
</script>

<style scoped>

    .containe {
        display: flex;
    }
    .league-cards {
        margin: 20px;
    }
    .info {
        flex: 80%;
    }
    h2 {
        border-bottom: 1px solid black;
        text-align: left;
        margin: 0 15px 0 15px;
    }
    .btn-add-league{
        margin: 0 15px 0 15px;
    }
</style>