const sampleSelect = document.getElementById('sampleSelect');
const modeInput = document.getElementById('mode');
const inputValue = document.getElementById('inputValue');
const keyInput = document.getElementById('keyInput');
const inputLabel = document.getElementById('inputLabel');
const inputHelp = document.getElementById('inputHelp');
const sampleInfo = document.getElementById('sampleInfo');
const inputChoice = document.getElementById('inputChoice');
const tabs = document.querySelectorAll('.tab');

function getMode(){ return modeInput.value || 'encrypt'; }
function getInputType(){ return document.querySelector('input[name="input_type"]:checked')?.value || 'hex'; }
function setInputType(type){
  const radio = document.querySelector(`input[name="input_type"][value="${type}"]`);
  if (radio) radio.checked = true;
}
function refreshLabels(){
  const mode = getMode();
  tabs.forEach(t => t.classList.toggle('active', t.dataset.mode === mode));
  if (mode === 'decrypt') {
    inputLabel.textContent = 'Ciphertext';
    inputHelp.textContent = 'Dekripsi wajib menerima ciphertext hex 32 karakter.';
    inputChoice.classList.add('disabled');
  } else {
    inputLabel.textContent = 'Plaintext';
    inputHelp.textContent = 'Plaintext boleh hex 32 karakter atau teks maksimal 16 karakter.';
    inputChoice.classList.remove('disabled');
  }
  updateNotice();
}
function updateNotice(){
  const sample = window.AES_SAMPLES[sampleSelect.value];
  if (!sample || sampleSelect.value === 'manual') {
    sampleInfo.textContent = 'Mode input manual: isi plaintext/ciphertext dan key sendiri untuk analisis.';
    return;
  }
  if (getMode() === 'encrypt') {
    sampleInfo.textContent = `Mode enkripsi: plaintext dan key otomatis diisi. Ciphertext benar: ${sample.cipher}`;
  } else {
    sampleInfo.textContent = `Mode dekripsi: ciphertext contoh otomatis diisi. Hasil plaintext yang benar: ${sample.expected_plain}`;
  }
}
function applySample(){
  const sample = window.AES_SAMPLES[sampleSelect.value];
  if (!sample || sampleSelect.value === 'manual') {
    updateNotice();
    return;
  }
  keyInput.value = sample.key;
  if (getMode() === 'decrypt') {
    setInputType('hex');
    inputValue.value = sample.cipher;
  } else {
    if (sample.plain_text) {
      setInputType('text');
      inputValue.value = sample.plain_text;
    } else {
      setInputType('hex');
      inputValue.value = sample.plain_hex;
    }
  }
  refreshLabels();
}

tabs.forEach(btn => btn.addEventListener('click', () => {
  modeInput.value = btn.dataset.mode;
  applySample();
}));
sampleSelect.addEventListener('change', applySample);
refreshLabels();

document.getElementById('resetBtn')?.addEventListener('click', () => {
  sampleSelect.value = 'manual';
  modeInput.value = 'encrypt';
  setInputType('hex');

  inputValue.value = '';
  keyInput.value = '';

  const outputSection = document.querySelector('.output');
  const detailsPanel = document.getElementById('detailsPanel');
  const alertBox = document.querySelector('.alert');

  if (outputSection) outputSection.remove();
  if (detailsPanel) detailsPanel.remove();
  if (alertBox) alertBox.remove();

  refreshLabels();
  updateNotice();
});

document.querySelectorAll('.copy').forEach(btn => btn.addEventListener('click', async () => {
  await navigator.clipboard.writeText(btn.dataset.copy);
  const old = btn.textContent;
  btn.textContent = 'TERSALIN!';
  setTimeout(() => btn.textContent = old, 1200);
}));

document.getElementById('toggleDetails')?.addEventListener('click', () => {
  const panel = document.getElementById('detailsPanel');
  if (!panel) return;
  panel.classList.toggle('hidden');
});
