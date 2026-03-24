<template>
  <div class="file-manager">
    <h2>File Manager</h2>
    <div class="upload-area" @dragover.prevent @drop="handleDrop">
      <p>Drag and drop files here to upload</p>
      <input type="file" @change="handleFileUpload" multiple />
    </div>
    <ul class="file-list">
      <li v-for="file in files" :key="file.name" class="file-item">
        <i :class="getFileIcon(file.type)"></i>
        <span>{{ file.name }} - {{ formatFileSize(file.size) }}</span>
        <button @click="downloadFile(file)">Download</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      files: [],
    };
  },
  methods: {
    handleFileUpload(event) {
      const selectedFiles = Array.from(event.target.files);
      this.files.push(...selectedFiles);
    },
    handleDrop(event) {
      const droppedFiles = Array.from(event.dataTransfer.files);
      this.files.push(...droppedFiles);
    },
    downloadFile(file) {
      // Implement file download functionality here 
    },
    getFileIcon(fileType) {
      // Map file types to icons
      const typeIcons = {
        'image/jpeg': 'icon-image',
        'image/png': 'icon-image',
        'application/pdf': 'icon-pdf',
        'application/vnd.ms-excel': 'icon-excel',
        'application/msword': 'icon-word',
        // Add more file types as needed
      };
      return typeIcons[fileType] || 'icon-file';
    },
    formatFileSize(size) {
      const sizes = ['Bytes', 'KB', 'MB', 'GB'];
      if (size === 0) return '0 Bytes';
      const i = parseInt(Math.floor(Math.log(size) / Math.log(1024)));
      return Math.round(size / Math.pow(1024, i)) + ' ' + sizes[i];
    },
  },
};
</script>

<style scoped>
.file-manager {
  padding: 20px;
}
.upload-area {
  border: 2px dashed #ccc;
  padding: 20px;
  text-align: center;
  margin-bottom: 20px;
}
.file-list {
  list-style-type: none;
  padding: 0;
}
.file-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 10px 0;
}
.icon-image {
  background: url('path-to-image-icon') no-repeat;
  width: 20px;
  height: 20px;
}
.icon-pdf {
  background: url('path-to-pdf-icon') no-repeat;
  width: 20px;
  height: 20px;
}
.icon-excel {
  background: url('path-to-excel-icon') no-repeat;
  width: 20px;
  height: 20px;
}
.icon-word {
  background: url('path-to-word-icon') no-repeat;
  width: 20px;
  height: 20px;
}
.icon-file {
  background: url('path-to-default-file-icon') no-repeat;
  width: 20px;
  height: 20px;
}
</style>