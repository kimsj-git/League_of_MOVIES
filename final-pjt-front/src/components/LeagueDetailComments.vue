<template>
	<div>
		<!-- <p>{{ comment }}</p> -->
		<div v-if="!isModifying">
			<hr>
			<p>작성자: {{ comment?.user.username }}</p>
			<p>내용: {{ comment?.content }}</p>
			<p>작성일: {{ comment?.created_at.substring(0, 10) }}</p>
			<v-btn @click.prevent="modifyComment">수정</v-btn>
			<v-btn @click.prevent="deleteComment">삭제</v-btn>
		</div>
		<div v-if="isModifying">
			<form @submit.prevent="createComment">
				<label for="modifyContent">댓글: </label>
				<textarea 
				class="form-control" 
				:value="comment.content" 
				@input="modifyContent=$event.target.value" 
				id="modifyContent" 
				cols="30" rows="3"
				></textarea>
				<input style="color: white;" @click="revComment(modifyContent)" value="수정">
			</form>
		</div> <br>

	</div>
</template>

<script>
import axios from 'axios'

const MATCH_URL = 'http://127.0.0.1:8000/api/v1/league'

export default {
	name: 'LeagueDetailComments',
	data() {
		return {
			isModifying: false,
			modifyContent: null,
		}
	},
	props: {
		comment: Object,
	},
	methods: {
		// getUserName()
		// deleteComment(commentId) {
		// axios({
		// 	method:'delete',
		// 	url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/comments/${commentId}`,
		// 	headers: {
		// 	Authorization: `Token ${ this.$store.state.token }`
		// 	},
		// })
		// 	.then((res) => {
		// 				console.log(res)
		// 				console.log(this.comment.match)
		// 				// this.$router.push({ path: `/league/${this.comment.match}` })
		// 				this.$router.go(this.$router.currentRoute)
		// 	})
		// 	.catch((err) => {
		// 	console.log(err)
		// 	})
		// },

		deleteComment : function() {
			let commentId = this.comment.id
			this.$emit('delete-comment', commentId)
		},
		modifyComment: function() {
			this.isModifying = true
		},
		revComment : function() {
			let commentId = this.comment.id
			let modifyContent = this.modifyContent
			this.$emit('modify-comment', commentId, modifyContent)
			this.isModifying = false
		},
		getComments() {
		axios({
			method:'get',
			url: `${MATCH_URL}/${this.comment.match}/comments/`,
			headers: {
			Authorization: `Token ${ this.$store.state.token }`
			}
		})
			.then((res) => {
			this.comments = res.data
			})
			.catch((err) => {
			console.log(err)
			})
		}, 
	}
}
</script>