import { createContext, useState } from 'react';
import './App.css';
import NoteTaker from './components/NoteTaker';
import RinaBadge from './components/RinaBadge';

export const RinaNoteContxt = createContext(null)

function App() {
  const initTemplateData = [
    { title: "APY.vision-IC backend", topics: ['Why blockchain?', 'startup lifestyle', 'high vol data exp'] },
    { title: "CryptoSat-Blockchain Engineer", topics: ['Solidity Exp', 'GoLang Exp', 'Python Exp', 'startup lifestyle'] },
    { title: "CryptoSat-Blockchain Engineer Blockchain Engineer", topics: ['Solidity Exp', 'GoLang Exp', 'Python Exp', 'startup lifestyle'] },
  ]

  const [template, setTemplate] = useState(null)
  const [templateOptions, setTemplateOptions] = useState(initTemplateData)
  const [note, setNote] = useState('')
  const [isRecording, setIsRecording] = useState(false)

  const [noteExpanded, setNoteExpanded] = useState(false)
  return (
    <RinaNoteContxt.Provider
      value={{
        template, setTemplate,
        templateOptions, setTemplateOptions,
        note, setNote,
        isRecording, setIsRecording
      }}
    >
      <div className="App">
        {noteExpanded ? <NoteTaker setNoteExpanded={setNoteExpanded} />
          : <RinaBadge setNoteExpanded={setNoteExpanded} />}
      </div>
    </RinaNoteContxt.Provider>
  );
}

export default App
