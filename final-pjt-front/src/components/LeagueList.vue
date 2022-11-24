<template>
    <div
    :style="{'background-image': 'url()'}"
  >
    <h2 style="color: white;">Movie League</h2>
    <v-carousel v-model="model" height="100%" continuous hide-delimiter-background>
      <v-carousel-item v-for="(match, i) in top3matches" :key="match.pk">
        <v-sheet height="100%" tile>
          <v-row class="fill-height" align="center" justify="center">
            <!-- <h5>TOP {{ i + 1 }}</h5> -->
            <LeagueListItem :match="match" />
            {{i}}
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <br>
    <h3 style="color: white;">Create new match here!</h3>
    <v-btn @click.prevent="goMatchCreate()">
      <v-icon>mdi-fencing</v-icon>START MATCH <v-icon>mdi-fencing</v-icon>
    </v-btn>
    <v-container style="width: 60%;">
      <LeagueListItem v-for="match in otherMatches" :key="match.id" :match="match" />
    </v-container>
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
    top3matches() {
      return this.$store.state.matches.slice(0, 3)
    },
    otherMatches() {
      return this.$store.state.matches.slice(3).reverse()
    },
  },
  methods: {
    goMatchCreate() {
      this.$router.push({ name: "CreateMatch" });
    },
  },
};
</script>