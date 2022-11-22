<template>
  <div>
    <h2>매치를 생성하세요</h2>
    <form @submit.prevent="createMatch">
      <!-- 서치 바에서 입력 -->

      <!-- 입력에 따라서 DB에서 검색한 영화들 표시, 2개 선택 -->

      <!-- 2개 선택 후 submit하면 요청 보내기 -->
      <input type="submit" value="매치 시작!">
    </form>


  </div>
</template>

<script>
export default {
  name: 'CreateMatch',
}
</script>

<style>

</style>