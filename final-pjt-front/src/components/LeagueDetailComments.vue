<template>
	<div>
		<p>------------------------------------</p>
		<!-- <p>{{ comment }}</p> -->
		<p>작성자: {{ comment?.user }}</p>
		<p>내용: {{ comment?.content }}</p>
		<p>작성시각: {{ comment?.created_at }}</p>
		<p>------------------------------------</p>
		<button @click.prevent="deleteComment(comment.id)">X</button>

	</div>
</template>

<script>
import axios from 'axios'

const MATCH_URL = 'http://127.0.0.1:8000/api/v1/league'

export default {
	name: 'LeagueDetailComments',
	data() {
		return {
		}
	},
	props: {
		comment: Object,
	},
	methods: {
		// getUserName()
    deleteComment(commentId) {
      axios({
        method:'delete',
        url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/comments/${commentId}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
        .then((res) => {
					console.log(res)
					console.log(this.comment.match)
					// this.$router.push({ path: `/league/${this.comment.match}` })
					this.$router.go(this.$router.currentRoute)
        })
        .catch((err) => {
          console.log(err)
        })
    } 
	}
}
</script>