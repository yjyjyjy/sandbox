const RinaBadge = ({ setNoteExpanded }) => {
    return (
        <div
            onClick={() => setNoteExpanded(true)}
            className='absolute h-16 w-16 left-10 top-10 shadow-lg rounded-full flex justify-center items-center bg-gradient-to-br from-sky-300 to-indigo-600 cursor-pointer'
            style={{ zIndex: 1000 }}
        >
            <span className='text-white text-lg font-bold'>Rina</span>
        </div>
    );
};

export default RinaBadge;