<template>
	<div>
		<p>------------------------------------</p>
		<p>작성자: {{ comment?.user }}</p>
		<p>내용: {{ comment?.content }}</p>
		<p>작성시각: {{ comment?.created_at }}</p>
	</div>
</template>

<script>
// import axios from 'axios'

// const MATCH_URL = 'http://127.0.0.1:8000/api/v1/league'

export default {
	name: 'LeagueDetailComments',
	data() {
		return {
		}
	},
	props: {
		comment: Object,
	},
}
</script>