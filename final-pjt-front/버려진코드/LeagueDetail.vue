    firstMovieVotersCount() {
       if (this.match.movie_1_voters) {
         return this.match.movie_1_voters.length
       }
     },
     secMovieVotersCount() {
       return this.match?.movie_2_voters?.length
     },