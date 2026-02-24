
<div style="padding: 16px; background: #f6f8fa; border-radius: 8px; margin: 20px 0;">
  <label for="folderName" style="font-weight: 600; color: #24292f; margin-right: 8px;">Project ID：</label>
  <input 
    type="text" 
    id="folderName" 
    placeholder="" 
    style="padding: 6px 10px; width: 300px; border: 1px solid #d0d7de; border-radius: 6px; outline: none;"
  >
  <button 
    onclick="jumpToProject()"
    style="margin-left: 8px; padding: 6px 16px; background: #2da44e; color: #fff; border: none; border-radius: 6px; cursor: pointer; font-weight: 500;"
  >
    GO
  </button>
  <p style="margin: 8px 0 0; font-size: 12px; color: #57606a;">Tip: Enter the exact project ID (case-sensitive) to jump directly to the corresponding project.</p>
  <!-- 核心跳转JS：拼接路径，无?path=参数 -->
  <script>
    function jumpToProject() {
      // 获取输入的项目ID（去除首尾空格，避免多余字符）
      const projectId = document.getElementById('folderName').value.trim();
      // 基础路径（固定不变）
      const baseUrl = 'https://www.bioinfo-lab.com/projects/';
      // 输入非空则跳转，否则提示
      if (projectId) {
        window.location.href = baseUrl + projectId;
      } else {
        alert('Please enter a valid Project ID!');
      }
    }
    // 新增：支持按回车键跳转（和点击GO按钮效果一致，更友好）
    document.getElementById('folderName').addEventListener('keydown', function(e) {
      if (e.key === 'Enter') jumpToProject();
    });
  </script>
</div>


<br>

### Updates:

* YAP-TEAD regulates the super-enhancer network to control early surface ectoderm commitment, **Nucleic Acids Research**, 2026.01, [paper](https://doi.org/10.1093/nar/gkaf1285), co-corresponding author [ZF]

<div align="center"><img src="https://www.bioinfo-lab.com/projects/img/nar_202601.jpeg" width='300'/></div><br>

* Single-nucleus profiling of mouse inner ear aging uncovers cell type heterogeneity and hair cell subtype-specific age-related signatures, **Cell Reports**, 2025.06, [paper](https://doi.org/10.1016/j.celrep.2025.115781), co-first author [ZF]

<div align="center"><img src="https://www.bioinfo-lab.com/projects/img/cellreports_202506.jpg" width='300'/></div><br>


