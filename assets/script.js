/* ========================================
   PNEUMONIA DETECTION - EXTERNAL JAVASCRIPT
   Save as: assets/script.js
   ======================================== */

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    console.log('🫁 Pneumonia Detection System Initialized');

    // Initialize all features
    initParticles();
    initImageEffects();
    initSoundEffects();
    initConfetti();
});

/* ==========================================
   PARTICLE BACKGROUND SYSTEM
   ========================================== */
function initParticles() {
    // Check if particles.js library is loaded
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            particles: {
                number: {
                    value: 100,
                    density: {
                        enable: true,
                        value_area: 800
                    }
                },
                color: {
                    value: '#ffffff'
                },
                shape: {
                    type: 'circle',
                    stroke: {
                        width: 0,
                        color: '#000000'
                    }
                },
                opacity: {
                    value: 0.4,
                    random: true,
                    anim: {
                        enable: true,
                        speed: 1,
                        opacity_min: 0.1,
                        sync: false
                    }
                },
                size: {
                    value: 3,
                    random: true,
                    anim: {
                        enable: true,
                        speed: 2,
                        size_min: 0.1,
                        sync: false
                    }
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#ffffff',
                    opacity: 0.3,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false,
                    attract: {
                        enable: false,
                        rotateX: 600,
                        rotateY: 1200
                    }
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: {
                        enable: true,
                        mode: 'repulse'
                    },
                    onclick: {
                        enable: true,
                        mode: 'push'
                    },
                    resize: true
                },
                modes: {
                    grab: {
                        distance: 400,
                        line_linked: {
                            opacity: 1
                        }
                    },
                    bubble: {
                        distance: 400,
                        size: 40,
                        duration: 2,
                        opacity: 8,
                        speed: 3
                    },
                    repulse: {
                        distance: 100,
                        duration: 0.4
                    },
                    push: {
                        particles_nb: 4
                    },
                    remove: {
                        particles_nb: 2
                    }
                }
            },
            retina_detect: true
        });

        console.log('✨ Particles initialized');
    }
}

/* ==========================================
   IMAGE HOVER EFFECTS
   ========================================== */
function initImageEffects() {
    // Add 3D tilt effect to images
    const images = document.querySelectorAll('.stImage img');

    images.forEach(img => {
        img.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;

            this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
        });

        img.addEventListener('mouseleave', function() {
            this.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
        });
    });

    console.log('🖼️ Image effects initialized');
}

/* ==========================================
   SOUND EFFECTS (Optional)
   ========================================== */
function initSoundEffects() {
    // Create audio context for sound effects
    const AudioContext = window.AudioContext || window.webkitAudioContext;

    if (AudioContext) {
        const audioContext = new AudioContext();

        // Success sound
        window.playSuccessSound = function() {
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();

            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);

            oscillator.frequency.value = 523.25; // C note
            oscillator.type = 'sine';

            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);

            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + 0.5);
        };

        // Warning sound
        window.playWarningSound = function() {
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();

            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);

            oscillator.frequency.value = 440; // A note
            oscillator.type = 'square';

            gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);

            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + 0.3);
        };

        console.log('🔊 Sound effects initialized');
    }
}

/* ==========================================
   CONFETTI CELEBRATION EFFECT
   ========================================== */
function initConfetti() {
    window.launchConfetti = function() {
        const duration = 3 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        const interval = setInterval(function() {
            const timeLeft = animationEnd - Date.now();

            if (timeLeft <= 0) {
                return clearInterval(interval);
            }

            const particleCount = 50 * (timeLeft / duration);

            // Create confetti from different positions
            confetti(Object.assign({}, defaults, {
                particleCount,
                origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }
            }));
            confetti(Object.assign({}, defaults, {
                particleCount,
                origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }
            }));
        }, 250);
    };

    console.log('🎉 Confetti system initialized');
}

/* ==========================================
   SMOOTH SCROLL ANIMATIONS
   ========================================== */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe all cards
    const cards = document.querySelectorAll('.glass-card, .info-card, .result-alert');
    cards.forEach(card => observer.observe(card));

    console.log('📜 Scroll animations initialized');
}

/* ==========================================
   TYPING EFFECT FOR TEXT
   ========================================== */
function typeWriter(element, text, speed = 50) {
    let i = 0;
    element.innerHTML = '';

    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

/* ==========================================
   PROGRESS BAR ANIMATION
   ========================================== */
function animateProgress(element, targetValue, duration = 1000) {
    const startValue = 0;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        const currentValue = startValue + (targetValue - startValue) * easeOutCubic(progress);
        element.style.width = currentValue + '%';

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
}

/* ==========================================
   PULSE EFFECT ON DETECTION
   ========================================== */
function pulseElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.classList.add('pulse-animation');
        setTimeout(() => {
            element.classList.remove('pulse-animation');
        }, 1000);
    }
}

/* ==========================================
   SCAN LINE EFFECT
   ========================================== */
function createScanEffect(container) {
    const scanLine = document.createElement('div');
    scanLine.className = 'scan-line';
    scanLine.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00ff00, transparent);
        box-shadow: 0 0 10px #00ff00;
        animation: scanLine 2s linear infinite;
    `;
    container.appendChild(scanLine);
}

/* ==========================================
   GLITCH TEXT EFFECT
   ========================================== */
function glitchText(element, duration = 500) {
    const originalText = element.textContent;
    const chars = '!<>-_\\/[]{}—=+*^?#________';

    let iterations = 0;
    const maxIterations = duration / 30;

    const interval = setInterval(() => {
        element.textContent = originalText
            .split('')
            .map((char, index) => {
                if (index < iterations) {
                    return originalText[index];
                }
                return chars[Math.floor(Math.random() * chars.length)];
            })
            .join('');

        iterations += 1;

        if (iterations > maxIterations) {
            clearInterval(interval);
            element.textContent = originalText;
        }
    }, 30);
}

/* ==========================================
   UTILITY FUNCTIONS
   ========================================== */

// Generate random color
function randomColor() {
    return '#' + Math.floor(Math.random()*16777215).toString(16);
}

// Shake element
function shakeElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.style.animation = 'shake 0.5s';
        setTimeout(() => {
            element.style.animation = '';
        }, 500);
    }
}

// Add CSS for shake animation
const style = document.createElement('style');
style.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
        20%, 40%, 60%, 80% { transform: translateX(10px); }
    }
    
    .pulse-animation {
        animation: pulse 1s ease-in-out;
    }
    
    .animate-in {
        animation: fadeIn 0.8s ease-out;
    }
`;
document.head.appendChild(style);

/* ==========================================
   EXPORT FUNCTIONS FOR STREAMLIT
   ========================================== */
window.pneumoniaDetection = {
    playSuccessSound: () => window.playSuccessSound && window.playSuccessSound(),
    playWarningSound: () => window.playWarningSound && window.playWarningSound(),
    launchConfetti: () => window.launchConfetti && window.launchConfetti(),
    pulseElement: pulseElement,
    shakeElement: shakeElement,
    glitchText: glitchText,
    typeWriter: typeWriter,
    animateProgress: animateProgress
};

console.log('✅ All systems initialized successfully!');