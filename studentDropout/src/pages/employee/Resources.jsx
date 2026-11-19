import React from "react";
import { Card } from "../../components/common/Card";
import { FileText, HeartHandshake, TrendingUp, ShieldCheck, ExternalLink, BookOpen, GraduationCap } from "lucide-react";

export const Resources = () => {
  const resourcesList = [
    {
      title: "Student Academic Handbook & Regulations",
      category: "Academic Policies",
      icon: BookOpen,
      description: "Comprehensive guide covering degree completion requirements, grading criteria, academic integrity, and course withdrawal policies.",
      color: "indigo",
    },
    {
      title: "Peer Mentorship & Tutoring Groups",
      category: "Learning Support",
      icon: GraduationCap,
      description: "Access academic tutoring sessions, peer study groups, departmental writing clinics, and peer mentoring tracks.",
      color: "purple",
    },
    {
      title: "Student Mental Health & Campus Wellness",
      category: "Wellbeing & Counseling",
      icon: HeartHandshake,
      description: "Campus counseling contact info, stress and exam anxiety management, wellness workshops, and student support lines.",
      color: "emerald",
    },
    {
      title: "Survey Privacy & Retention Ethics",
      category: "Data Privacy",
      icon: ShieldCheck,
      description: "Learn how DropGuard securely processes student wellbeing surveys and enables counselors to intervene before academic distress leads to dropout.",
      color: "amber",
    },
  ];

  return (
    <div className="max-w-4xl space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900">Academic & Student Wellbeing Resources</h2>
        <p className="text-xs text-slate-500">Academic guidelines, tutoring resources, stress management, and counseling support</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {resourcesList.map((item, index) => {
          const Icon = item.icon;
          return (
            <Card key={index} className="hover:border-indigo-200 transition-all flex flex-col justify-between">
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded-full border border-indigo-100">
                    {item.category}
                  </span>
                  <Icon className="w-5 h-5 text-slate-400" />
                </div>
                <h3 className="text-base font-bold text-slate-800">{item.title}</h3>
                <p className="text-xs text-slate-500 leading-relaxed">{item.description}</p>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-indigo-600">
                <span>Access Resource</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </div>
            </Card>
          );
        })}
      </div>
    </div>
  );
};
