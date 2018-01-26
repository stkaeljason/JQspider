<template>
  <div class="addtask">
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入参数" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addTask()" style="float:left; margin: 2px;">新增加法任务</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'AddTask',
  data () {
     return {
     msg: 'Welcome to wyyx_spider'
    }
  },
  methods: {
    addTask(){
      this.$http.get('http://127.0.0.1:8000/api/add_task' + this.input)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.$message.error('新增任务成功')
            } else {
              this.$message.error('新增任务失败，请重试')
              console.log(res['msg'])
            }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
