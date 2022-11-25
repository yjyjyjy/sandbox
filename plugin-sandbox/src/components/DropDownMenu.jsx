import { Fragment, useState } from 'react'
import { Menu, Transition } from '@headlessui/react'
import { BiChevronDown } from "react-icons/bi";




const DropDownMenu = () => {

    const [options, setOptions] = useState([
        { label: "Backend Eng", active: false },
        { label: "Frontend Eng", active: false },
        { label: "Data Eng", active: false },
    ])

    let selected
    if (options) {
        const active = options.filter(op => op.active)
        if (active.length > 0) {
            selected = active[0].label
        }
    }

    const onMenuItemSelected = (label) => {
        const newOptions = [...options]
        const objIndex = newOptions.findIndex(obj => obj.label === label)
        newOptions.forEach(obj => {
            obj.active = false
        });
        newOptions[objIndex].active = true
        setOptions(newOptions)
    }

    const DropDownMenuItem = ({ label, active }) => (
        <Menu.Item>
            {() => (
                <div
                    onClick={() => onMenuItemSelected(label)}
                    className={
                        `${(active ? 'bg-gray-100 text-gray-900' : 'text-gray-700')
                            .concat(' ', 'block px-4 py-2 text-sm cursor-pointer')}`
                    }
                >
                    {label}
                </div>
            )}
        </Menu.Item>
    )



    return (
        <Menu as="div" className="relative inline-block text-left">
            <div>
                <Menu.Button className="inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-2 py-1 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100">
                    {!!selected ? selected : "Choose a template"}
                    <BiChevronDown className="-mr-1 ml-1 h-5 w-5" aria-hidden="true" />
                </Menu.Button>
            </div>

            <Transition
                as={Fragment}
                enter="transition ease-out duration-100"
                enterFrom="transform opacity-0 scale-95"
                enterTo="transform opacity-100 scale-100"
                leave="transition ease-in duration-75"
                leaveFrom="transform opacity-100 scale-100"
                leaveTo="transform opacity-0 scale-95"
            >
                <Menu.Items className="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <div className="py-1">
                        {options.map(
                            (opt, idx) => <DropDownMenuItem index={idx} label={opt.label} active={opt.active} />
                        )}
                        {/* <DropDownMenuItem active={true} label={'Account'} />
                        <DropDownMenuItem active={false} label={'Settings'} /> */}
                    </div>
                </Menu.Items>
            </Transition>
        </Menu>
    );
};

export default DropDownMenu;