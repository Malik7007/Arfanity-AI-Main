const { app, BrowserWindow, ipcMain, globalShortcut, Menu, Tray } = require('electron');
const path = require('path');
const isDev = !app.isPackaged;

let mainWindow;
let tray;

function createWindow() {
	mainWindow = new BrowserWindow({
		width: 1200,
		height: 800,
		titleBarStyle: 'hiddenInset',
		webPreferences: {
			preload: path.join(__dirname, 'preload.cjs'),
			contextIsolation: true,
			nodeIntegration: false
		},
		icon: path.join(__dirname, '../static/favicon.png')
	});

	const url = isDev ? 'http://localhost:5173' : `file://${path.join(__dirname, '../build/index.html')}`;
	mainWindow.loadURL(url);

	if (isDev) {
		mainWindow.webContents.openDevTools();
	}

	mainWindow.on('closed', () => {
		mainWindow = null;
	});
}

function createTray() {
	tray = new Tray(path.join(__dirname, '../static/favicon.png'));
	const contextMenu = Menu.buildFromTemplate([
		{ label: 'Open Arfanity AI', click: () => mainWindow.show() },
		{ type: 'separator' },
		{ label: 'Quit', click: () => app.quit() }
	]);
	tray.setToolTip('Arfanity AI');
	tray.setContextMenu(contextMenu);
}

app.whenReady().then(() => {
	createWindow();
	createTray();

	// Global Hotkey (Alt+Space)
	globalShortcut.register('Alt+Space', () => {
		if (mainWindow.isVisible()) {
			mainWindow.hide();
		} else {
			mainWindow.show();
			mainWindow.focus();
		}
	});

	app.on('activate', () => {
		if (BrowserWindow.getAllWindows().length === 0) createWindow();
	});
});

app.on('window-all-closed', () => {
	if (process.platform !== 'darwin') app.quit();
});

ipcMain.handle('get-app-version', () => app.getVersion());
