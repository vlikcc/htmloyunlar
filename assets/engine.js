export const GameEngine = {
	state: { score: 0, level: "easy", muted: false },
	init({ onStart, onReset } = {}) {
		this.onStart = onStart || (() => {});
		this.onReset = onReset || (() => {});
		this.bindGlobalUI();
	},
	bindGlobalUI() {
		document.addEventListener("click", (e) => {
			const target = e.target;
			if (!(target instanceof HTMLElement)) return;
			if (target.matches("[data-action=toggle-audio]")) {
				this.state.muted = !this.state.muted;
				window.localStorage.setItem("muted", String(this.state.muted));
			}
			if (target.matches("[data-action=start]")) this.onStart?.();
			if (target.matches("[data-action=reset]")) this.onReset?.();
		});
	},
	addScore(points) {
		this.state.score += points;
		window.dispatchEvent(new CustomEvent("score:change", { detail: this.state.score }));
		window.localStorage.setItem("lastScore", String(this.state.score));
	},
	resetScore() {
		this.state.score = 0;
		window.dispatchEvent(new CustomEvent("score:change", { detail: this.state.score }));
	}
};

export const Timer = {
	seconds: 0,
	intervalId: null,
	start(durationSeconds, onTick, onEnd) {
		this.stop();
		this.seconds = durationSeconds;
		onTick?.(this.seconds);
		this.intervalId = window.setInterval(() => {
			this.seconds -= 1;
			onTick?.(this.seconds);
			if (this.seconds <= 0) {
				this.stop();
				onEnd?.();
			}
		}, 1000);
	},
	stop() { if (this.intervalId) { window.clearInterval(this.intervalId); this.intervalId = null; } },
	reset() { this.stop(); this.seconds = 0; }
};

export const AudioFx = {
	play(id) {
		const el = document.getElementById(id);
		if (el instanceof HTMLAudioElement) {
			const muted = window.localStorage.getItem("muted") === "true";
			if (!muted) el.currentTime = 0, el.play().catch(() => {});
		}
	}
};

export const Storage = {
	get(key, fallback = null) {
		try { return JSON.parse(localStorage.getItem(key) ?? "null") ?? fallback; } catch { return fallback; }
	},
	set(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* ignore */ } }
};

export function $(selector, root = document) { return root.querySelector(selector); }
export function $all(selector, root = document) { return Array.from(root.querySelectorAll(selector)); }