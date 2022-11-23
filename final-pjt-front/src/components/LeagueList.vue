<template>
  <div>
    <h2>Movie League</h2>
    <v-btn @click.prevent="goMatchCreate()">
      <v-icon>mdi-fencing</v-icon>매치 만들기 <v-icon>mdi-fencing</v-icon>
    </v-btn>
    <hr>
    <v-carousel v-model="model">
      <v-carousel-item v-for="(match, i) in matches" :key="match.pk">
        <v-sheet :color="color" height="100%" tile>
          <v-row class="fill-height" align="center" justify="center">
            {{ i + 1 }}번째 매치
            <LeagueListItem :match="match" />
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <!-- <v-container>
      <LeagueListItem v-for="match in matches" :key="match.id" :match="match" />
    </v-container> -->
  </div>
</template>

<script>
import LeagueListItem from "@/components/LeagueListItem";
// import CreateMatch from '@/components/CreateMatch'

export default {
  name: "LeagueList",
  data() {
    return {
      model: 0,
      colors: [
        "primary", 
        "secondary", 
        "yellow darken-2", 
        "red", 
        "orange"],
    };
  },
  components: {
    LeagueListItem,
    // CreateMatch,
  },
  computed: {
    matches() {
      // console.log(this.$store.state.movies)
      return this.$store.state.matches;
    },
  },
  methods: {
    goMatchCreate() {
      this.$router.push({ name: "CreateMatch" });
    },
  },
};
</script>