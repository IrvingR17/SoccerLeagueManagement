<template lang="">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de jugadores</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="players" :fields="fields">

                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            players: [],
            fields: [
                {key: 'user.first_name', label: 'Nombre'},
                {key: 'user.last_name', label: 'Apellido'},
                {key: 'user.email', label: 'Correo Electronico'},
            ]
        }
    },
    methods: {
        getPlayers() {
            const path = 'http://127.0.0.1:8000/api/players/list/'
            axios.get(path).then((response) => {
                this.players = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getPlayers()
    },
}
</script>
<style lang="">
    
</style>