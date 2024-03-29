import { Fragment, useContext } from 'react'
import { Menu, Transition } from '@headlessui/react'
import { BiChevronDown } from "react-icons/bi";
import { RinaNoteContxt } from '../App';

const DropDownMenu = () => {
    const { template, setTemplate, templateOptions, setNote } = useContext(RinaNoteContxt)

    const DropDownMenuItem = ({ label, active }) => (
        <Menu.Item>
            {() => (
                <div
                    onClick={() => {
                        setTemplate(label)
                        const templateContentString = templateOptions
                            .filter(opt => opt.title === label)[0]
                            .topics
                            .map(tp => '- '.concat(tp))
                            .join("\r\n".repeat(3))
                        setNote(templateContentString)
                    }}
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
                <Menu.Button className="inline-flex w-full mx-2 justify-center rounded-md border border-gray-300 bg-white px-2 py-1 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100">
                    <span className='truncate w-40'>
                        {!!template ? template : "Choose a template"}
                    </span>
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
                        {templateOptions.map(t => t.title).map(
                            (opt, idx) => <DropDownMenuItem key={idx} label={opt} active={opt === template} />
                        )}
                    </div>
                </Menu.Items>
            </Transition>
        </Menu>
    );
};

export default DropDownMenu;


