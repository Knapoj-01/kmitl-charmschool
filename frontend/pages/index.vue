<template>
<div class='container'>
  abcdefgadfasdf
  {{reviewers}}
  </div>
</template>

<script>
export default {
  data(){
    return {
      reviewers: []
    }
  },
  async fetch() {
    this.reviewers = await fetch('https://localhost:8000/auth/user/').then((res) => res.json())
  }
}

</script>
