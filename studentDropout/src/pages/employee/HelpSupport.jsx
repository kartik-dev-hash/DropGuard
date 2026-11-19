import React, { useState } from "react";
import { Card } from "../../components/common/Card";
import { Toast } from "../../components/common/Toast";
import { HelpCircle, ChevronDown, ChevronUp, Send } from "lucide-react";

export const HelpSupport = () => {
  const [openFaq, setOpenFaq] = useState(null);
  const [ticketSent, setTicketSent] = useState(false);
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");

  const faqs = [
    {
      q: "Is my wellbeing survey confidential?",
      a: "Yes. Your responses are processed securely through DropGuard to assist academic counselors in supporting student retention, learning engagement, and student wellbeing.",
    },
    {
      q: "How often should I submit the wellbeing survey?",
      a: "Check-in surveys are conducted each academic semester or whenever initiated by your institution's academic counseling department.",
    },
    {
      q: "Can I update my survey responses after submission?",
      a: "Once submitted, responses are recorded for counselor review. If you have immediate questions or need to make an update, contact your assigned academic counselor.",
    },
    {
      q: "Who sees my survey ratings?",
      a: "Responses are reviewed by authorized Academic Counselors and Advisors belonging to your institution.",
    },
  ];

  const handleSendTicket = (e) => {
    e.preventDefault();
    setTicketSent(true);
    setSubject("");
    setMessage("");
  };

  return (
    <div className="max-w-4xl space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900">Help & Academic Support</h2>
        <p className="text-xs text-slate-500">Frequently asked questions and direct academic advisor assistance</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* FAQs */}
        <div className="md:col-span-2 space-y-4">
          <Card title="Frequently Asked Questions">
            <div className="space-y-3">
              {faqs.map((faq, index) => {
                const isOpen = openFaq === index;
                return (
                  <div
                    key={index}
                    className="border border-slate-100 rounded-2xl overflow-hidden transition-all bg-slate-50/50"
                  >
                    <button
                      onClick={() => setOpenFaq(isOpen ? null : index)}
                      className="w-full p-4 text-left flex items-center justify-between gap-3 text-xs sm:text-sm font-bold text-slate-800 hover:bg-slate-100/50 transition-colors cursor-pointer"
                    >
                      <span className="flex items-center gap-2">
                        <HelpCircle className="w-4 h-4 text-indigo-600 flex-shrink-0" />
                        {faq.q}
                      </span>
                      {isOpen ? (
                        <ChevronUp className="w-4 h-4 text-slate-400 flex-shrink-0" />
                      ) : (
                        <ChevronDown className="w-4 h-4 text-slate-400 flex-shrink-0" />
                      )}
                    </button>

                    {isOpen && (
                      <div className="p-4 pt-0 text-xs text-slate-600 leading-relaxed border-t border-slate-100 bg-white">
                        {faq.a}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </Card>
        </div>

        {/* Contact Counselor Ticket Box */}
        <div>
          <Card title="Contact Academic Counselor">
            {ticketSent && (
              <Toast
                type="success"
                message="Support message sent to your academic counseling team!"
                onClose={() => setTicketSent(false)}
              />
            )}
            <form onSubmit={handleSendTicket} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Subject</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Course difficulty query"
                  value={subject}
                  onChange={(e) => setSubject(e.target.value)}
                  className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Message</label>
                <textarea
                  required
                  rows="3"
                  placeholder="Describe your request..."
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white resize-none"
                />
              </div>

              <button
                type="submit"
                className="w-full py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer"
              >
                <Send className="w-3.5 h-3.5" />
                <span>Send Message</span>
              </button>
            </form>
          </Card>
        </div>
      </div>
    </div>
  );
};
