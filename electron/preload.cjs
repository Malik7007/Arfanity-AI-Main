const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
	getAppVersion: () => ipcRenderer.invoke('get-app-version'),
	sendNotification: (title, body) => {
		new Notification(title, { body });
	}
});
