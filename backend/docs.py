"""
This module contains a centralized list of all policy documents.
Each document is represented as a dictionary containing its filename, title, and brief description.
This list provides the necessary context for the AI model to accurately
identify relevant documents for a given audit question.
"""

DOCUMENTS = [
    # AA Folder
    {'filename': "AA.1000_CEO20250206_v20250201.pdf", 'title': "Medi-Cal Glossary of Terms"},
    {
        'filename': "AA.1204_20240725_v20240701.pdf",
        'title': "Gifts, Honoraria, and Travel\nPayments",
        'description': "This policy ensures CalOptima Health employees and officials comply with legal and ethical limits regarding honoraria, gifts, or travel payments from outside sources, aiming to avoid conflicts of interest. It prohibits the receipt of honoraria and gifts exceeding $5.00 in a calendar year, with certain exceptions."
    },
    {
        'filename': "AA.1207a_CEO20240605_v2024060.pdf",
        'title': "CalOptima Health Auto-Assignment",
        'description': "This policy establishes the process CalOptima Health will use to automatically assign members who have not selected a Health Network or CHCN to one. The auto-assignment process prioritizes member access to care, community health center participation, and enrollment in high-quality networks. Members can request to change their assigned network once per month."
    },
    {
        'filename': "AA.1207b_CEO20241113_v20241107.pdf",
        'title': "Performance-based Health\nNetwork and CalOptima Health\nCommunity Network Auto-\nAssignment Allocation\nMethodology",
        'description': "This policy outlines CalOptima Health's methodology for allocating Health Network and Community Network assignments based on performance indicators. It details how Auto-Assignment Quality Scores (AAQS) are calculated and utilized to determine the order in which members are assigned to networks. The policy also addresses scenarios such as suspension of Auto-Assignment and the allocation process for new Health Networks."
    },
    {
        'filename': "AA.1207c_CEO20241113_v20241107.pdf",
        'title': "Performance-based Community Health Center Auto-Assignment Allocation Methodology",
        'description': "This policy establishes CalOptima Health’s methodology for determining a Community Health Center’s Auto-Assignment allocation according to performance-based indicators. It outlines how members are auto-assigned based on performance metrics and ensures Federally Qualified Health Centers receive a higher allocation. The policy also details the calculation of the Auto Assignment Quality Score (AAQS) and the annual evaluation process."
    },
    {
        'filename': "AA.1208_CEO20240808_v20240801.pdf",
        'title': "Non-Monetary Member Incentives",
        'description': "This policy establishes CalOptima Health’s standards for the appropriate use of non-monetary incentives for Medi-Cal members to enhance health education programs and increase member participation, learning, and motivation. It outlines guidelines that CalOptima Health and its Health Networks must follow regarding the use of these incentives, ensuring compliance with DHCS guidelines and preventing incentives that encourage enrollment."
    },
    {
        'filename': "AA.1214_CEO20241216_v20241201.pdf",
        'title': "Guidelines for Endorsements by\nCalOptima Health, for Letters\nof Support and Use of\nCalOptima Health Name or\nLogo",
        'description': "This policy outlines the guidelines for CalOptima Health endorsements to external entities, including Letters of Support and the use of the CalOptima Health name or logo. It aims to protect the organization's reputation and ensure that endorsements align with its mission and purpose, while also restricting unauthorized use of its name and logo."
    },
    {
        'filename': "AA.1215_20240725_v20240701.pdf",
        'title': "Public Records Requests and\nSubpoenas",
        'description': "This policy establishes guidelines for responding to requests for CalOptima Health's records under the Public Records Act and/or a subpoena. It outlines the process for accessing non-exempt public records and responding to lawful subpoenas while adhering to privacy and legal requirements."
    },
    {
        'filename': "AA.1216_CEO20240725_v20240701.pdf",
        'title': "Solicitation and Receipt of Gifts\nto CalOptima Health",
        'description': "This policy defines the criteria and procedures for receiving gifts from outside sources, in accordance with the Political Reform Act and the Federal Anti-Kickback Statute. It outlines acceptable and prohibited gifts, as well as the conditions under which CalOptima Health can solicit or receive gifts, ensuring impartiality and alignment with the organization's mission."
    },
    {
        'filename': "AA.1217_CEO20240725_v20240701.pdf",
        'title': "Legal Claims and Judicial Review",
        'description': "This policy outlines the process for presenting legal claims to CalOptima Health, ensuring compliance with California Government Code and other applicable regulations. It covers the presentation of claims, exceptions, timeliness, and procedures for late or insufficient claims, also addressing judicial review processes."
    },
    {
        'filename': "AA.1219a_CEO20240912_v20240901.pdf",
        'title': "Member Advisory Committee",
        'description': "This policy outlines the purpose, composition, and responsibilities of CalOptima Health's Member Advisory Committee (MAC). It establishes a process for recruiting and selecting MAC members and describes how the MAC provides advice and recommendations to the CalOptima Health Board regarding programs and policies affecting quality and health equity."
    },
    {
        'filename': "AA.1219b_v20240301_CEO20240424.pdf",
        'title': "Provider Advisory Committee",
        'description': "This policy outlines the purpose, composition, and function of CalOptima Health's Provider Advisory Committee (PAC). It establishes a process for recruiting, evaluating, and selecting PAC members and defines the committee's role in providing advice and recommendations to the CalOptima Health Board of Directors regarding the organization's programs."
    },
    {
        'filename': "AA.1220_CEO20240620_v20240401.pdf",
        'title': "Member Billing",
        'description': "This policy outlines the specific situations where a CalOptima Health member may or may not be billed for healthcare services. It clarifies that members generally should not be billed for covered services, except under certain circumstances such as non-covered services or services agreed upon in writing."
    },
    {
        'filename': "AA.1223_CEO20241216_v20241201.pdf",
        'title': "Participation in Community Events by External Entities",
        'description': "This policy outlines the guidelines for CalOptima Health's involvement in community events and activities with external organizations. It specifies eligibility criteria for external entities seeking CalOptima Health's participation and ensures alignment with the organization's mission, vision, and values while adhering to fiscal responsibilities."
    },
    {
        'filename': "AA.1251_CEO20250306_v20250301.pdf",
        'title': "Diversity, Equity, and Inclusion Training Program",
        'description': "This policy outlines CalOptima Health's Diversity, Equity, and Inclusion (DEI) Training program. It ensures that all CalOptima Health Employees, Subcontractors, Downstream Subcontractors, and Network Providers are trained on DEI standards, cultural competency, and health equity, in accordance with applicable regulations."
    },
    {
        'filename': "AA.1270_CEO20241119_v20241107.pdf",
        'title': "Certification of Document and\nData Submissions",
        'description': "This policy outlines the process for CalOptima Health to certify data, information, and documentation submitted to the Department of Health Care Services (DHCS). It specifies which data must be certified and who is authorized to sign the certification statement, ensuring compliance with federal regulations and contractual requirements. The certification covers a wide range of data related to encounter data, provider networks, service accessibility, rate determination, financial status, and more."
    },
    {
        'filename': "AA.1271_CEO20250129_v20250101.pdf",
        'title': "Whole-Child Model Family Advisory Committee",
        'description': "This policy outlines the purpose, composition, and responsibilities of the Whole-Child Model Family Advisory Committee (WCM FAC), which advises the CalOptima Health Board on California Children’s Services (CCS) provided through the WCM program. It establishes a process for recruiting, evaluating, and selecting candidates for the WCM FAC, ensuring representation of diverse cultural backgrounds and special needs within the Whole-Child Model population."
    },
    {
        'filename': "AA.1275_CEO20241119_v20241107.pdf",
        'title': "Department of Health Care Services (DHCS) File and Use Submission Process",
        'description': "This policy outlines CalOptima Health’s process for submitting materials to the Department of Health Care Services (DHCS) through the File and Use process. It details the types of Medi-Cal materials that can be submitted, including policies with minor revisions and consent forms. The policy also describes the procedure for submitting these materials to the Regulatory Affairs & Compliance Policies and Procedures (RAC P&P) team."
    },
    {
        'filename': "AA.1400_CEO20241205_v20241205.pdf",
        'title': "Grant Management",
        'description': "This policy outlines the criteria for awarding Grant funds and the expectations of Grantees for discretionary Grant funding disbursed by CalOptima Health. It also covers ethical considerations, including conflict of interest, gratuities, and confidentiality. The policy applies to administrative functions."
    },

    # CMC Folder
    {
        'filename': "CMC.9002__Policy_CEO20220818_DHCS20220701_PRC20220518_v.20220501_CEO.pdf",
        'title': "Member Grievance Process",
        'description': "This policy defines CalOptima's process for addressing and resolving OneCare Connect Member Grievances, adhering to regulatory requirements from CMS and DHCS. It covers the receipt, handling, and resolution of grievances related to various aspects of CalOptima's operations, healthcare services, and benefits."
    },
    {
        'filename': "CMC.3001_CEO20240523.pdf",
        'title': "Payment Arrangements to Health Networks – Capitation Payments",
        'description': "This policy outlines the process for timely and accurate capitation payments made by CalOptima Health to Health Networks, as specified in their Cal MediConnect Health Network Contract. It details how payments are calculated based on Medicare and Medi-Cal components, adjustments for member enrollment changes, and potential deductions or recoupments."
    },
    {
        'filename': "CMC.9003__Policy_CEO20220818_DHCS20220701_PRC20220518_v.20220501_CEO.pdf",
        'title': "Standard Appeal",
        'description': "This policy outlines CalOptima's standard appeal process for OneCare Connect members, ensuring access to a clear and reliable system for Medicare and Medi-Cal covered services. The policy details the handling, tracking, and resolution of appeals in compliance with applicable regulations and contractual requirements from CMS and DHCS."
    },
    {
        'filename': "CMC.9005__Policy_CEO20220818_DHCS20220701_PRC20220518_v.20220501_CEO.pdf",
        'title': "Payment Appeal",
        'description': "This policy outlines CalOptima's process for ensuring Members have access to a Payment Appeal process for Medicare and Medi-Cal Covered Services, meeting the requirements of CMS and DHCS. It establishes procedures for handling Payment Appeals, including receipt, tracking, and disposition, in accordance with applicable statutes and regulations."
    },

    # DD Folder
    {
        'filename': "DD.2001_CEO20240515_no attachments.pdf",
        'title': "Member Rights and\nResponsibilities",
        'description': "This policy outlines the rights and responsibilities of CalOptima Health members and details how CalOptima Health communicates these rights. It ensures that members are informed and their rights are respected within the CalOptima Health network. The policy covers various aspects, including access to care, grievance procedures, and privacy protections."
    },
    {
        'filename': "DD.2002_CEO20250206_v20241231.pdf",
        'title': "Cultural and Linguistic Services",
        'description': "This policy defines CalOptima Health’s Cultural and Linguistic (C&L) program and describes the processes in place to continually monitor, improve and evaluate C&L services that support the delivery of Covered Services to CalOptima Health Members. It outlines requirements for providing culturally and linguistically appropriate services to members, including bilingual staff, interpreter services, and translated materials."
    },
    {
        'filename': "DD.2003_CEO20241216_v20241201.pdf",
        'title': "Member Identification and\nEligibility Verification",
        'description': "This policy outlines the process for Providers to verify a Member’s eligibility to receive Covered Services from CalOptima Health. It details the issuance and content of member ID cards, methods for eligibility verification, and actions taken upon notification of a member's death."
    },
    {
        'filename': "DD.2004_CEO20241031_v20241001.pdf",
        'title': "CalOptima Health Member Orientation",
        'description': "This policy outlines the process for scheduling, conducting, evaluating, and revising CalOptima Health Member orientations. It ensures members receive appropriate and timely information on covered services and a better understanding of their healthcare delivery system. The policy details requirements for conducting orientations in multiple languages and offering alternative methods for members unable to attend in person."
    },
    {
        'filename': "DD.2005_CEO20241216_v20241201.pdf",
        'title': "Member Informing Materials",
        'description': "This policy defines the distribution requirements for the CalOptima Health Provider Directory and Formulary, as well as the content and distribution requirements for the CalOptima Health Member Handbook and the Health Networks’ Member Welcome Letter. It outlines specific information that must be included in the Member Handbook, as required by the Department of Health Care Services (DHCS)."
    },
    {
        'filename': "DD.2006_CEO20241216_v20241201.pdf",
        'title': "Enrollment In/Eligibility with\nCalOptima Health Direct",
        'description': "This policy outlines the criteria for enrolling members in CalOptima Health Direct. It specifies the circumstances under which members are enrolled in either CalOptima Health Direct Administrative (COHD-A) or a CalOptima Health Community Network (CHCN), as well as conditions for excluding members from this policy."
    },
    {
        'filename': "DD.2006b_CEO20241205_v20241205.pdf",
        'title': "CalOptima Health Community\nNetwork Member Primary Care\nProvider Selection/Assignment",
        'description': "This policy outlines the criteria by which a CalOptima Health Community Network (CHCN) Member selects or is assigned a Primary Care Provider (PCP). It emphasizes the importance of establishing a medical home and maintaining continuity of care with a PCP, allowing members to select or be assigned a participating PCP."
    },
    {
        'filename': "DD.2008_CEO20241216_v20241201.pdf",
        'title': "Health Network and\nCalOptima Health Community\nNetwork Selection Process",
        'description': "This policy outlines the process by which eligible members can select a CalOptima Health Community Network (CHCN) or a Health Network, and details the responsibilities of the CHCN or Health Network towards the member. It emphasizes the member's right to choose a network and the importance of establishing a medical home with a Primary Care Provider (PCP)."
    },
    {
        'filename': "DD.2012_CEO20241216_v20241201.pdf",
        'title': "Member Notification of Change in Location or Availability of Providers or Covered Services",
        'description': "This policy outlines the process by which CalOptima Health or a Health Network will notify members of changes in the location or availability of providers or covered services.  It details the requirements for providing timely written notice to impacted members, including specific timelines and circumstances. The policy also addresses situations involving contract terminations, facility decertifications, and suspensions."
    },
    {
        'filename': "DD.2013_CEO20241031_v20241001.pdf",
        'title': "Customer Service Grievance Process",
        'description': "This policy outlines the process by which CalOptima Health's Customer Service Department intakes, addresses, resolves, and tracks grievances from members, their authorized representatives, or providers acting on their behalf. It ensures compliance with applicable statutory, regulatory, and contractual requirements and distinguishes grievances from inquiries."
    },
    {
        'filename': "DD.2014_CEO20250206_v20250101.pdf",
        'title': "Collection of Race, Ethnicity,\nLanguage, Sexual Orientation\nand Gender Identity Data",
        'description': "This policy outlines CalOptima Health’s process for collecting race/ethnicity, language (REL) and sexual orientation and gender identity (SOGI) data. It describes the use of an Electronic Health Information system that receives individual‐level REL and SOGI data, stores the data securely, and retrieves the data for reporting and analysis. The policy also covers data reconciliation, storage, direct data collection, and reporting requirements."
    },

    # EE Folder
    {
        'filename': "EE.1101_CEO20241205_v20241205.pdf",
        'title': "Additions, Changes, and\nTerminations to CalOptima Health\nProvider Information, CalOptima\nHealth Provider Directory, and\nWeb-based Directory",
        'description': "This policy outlines the process for adding, changing, or terminating a Provider in the CalOptima Health Provider Directory and Web-based Directory. It details requirements for publishing and updating the Provider Directory, ensuring it meets CMS and DHCS standards. The policy also covers the submission of the Medi-Cal Provider Directory to DHCS and the updating of the Medi-Cal Provider Directory Application Programming Interface (API)."
    },
    {
        'filename': "EE.1103_CEO20250129_v20250101.pdf",
        'title': "Provider Network Training",
        'description': "This policy outlines the education and training requirements for newly contracted providers and annual training provided by CalOptima Health to medical, behavioral health, and Long-Term Services and Support (LTSS) Providers. It applies to providers who interact with CalOptima Health Members and Subcontractors who serve CalOptima Health’s Members participating in Medi-Cal, OneCare and PACE programs, in accordance with applicable DHCS and CMS requirements."
    },
    {
        'filename': "EE.1106_v20240401_CEO20240417_no attachments.pdf",
        'title': "Health Network and CalOptima Health Community Network Minimum and Maximum Member Enrollment",
        'description': "This policy outlines the minimum and maximum member enrollment requirements for Health Networks and CalOptima Health Community Networks (CHCN). It ensures the viability of Health Networks by setting a minimum enrollment threshold and restricts maximum enrollment to maintain balance and prevent dominance by a single network or affiliated entities."
    },
    {
        'filename': "EE.1111_CEO20240523.pdf",
        'title': "Health Network Encounter Reporting Requirements",
        'description': "This policy outlines the guidelines and timeframes for Health Networks to submit Encounter data to CalOptima Health. It specifies the types of Encounter data required from different Health Network types and sets deadlines for submission and correction. Non-compliance may result in sanctions."
    },
    {
        'filename': "EE.1112_CEO20240523.pdf",
        'title': "Health Network Eligible Member Assignment to Primary Care Provider",
        'description': "This policy outlines the guidelines for Health Networks to assign members to Primary Care Providers (PCPs) and report these assignments to CalOptima Health. It covers member choice of PCP, assignment procedures for members who do not select a PCP, and considerations for PCP assignment, including geographic location, language preference, and age."
    },
    {
        'filename': "EE.1116_CEO20241122_v20241101.pdf",
        'title': "Contracted Provider Notification to\nCalOptima Health of Changes Affecting\nthe Legal Status of the Contract",
        'description': "This policy defines the process for Contracted Providers to notify CalOptima Health of changes affecting their legal status. It outlines the types of changes that require notification, such as changes in NPI, TIN, ownership, or legal name. The policy also details the procedure for the Contracting Department to handle these notifications, including acknowledgment, contract updates, and necessary approvals."
    },
    {
        'filename': "EE.1119_v20240301_CEO20240307_no attachments.pdf",
        'title': "Health Network Notification of\nAdministrative and Operational\nChanges",
        'description': "This policy outlines the process and requirements for Health Networks and Delegated Entities to report administrative and operational changes to CalOptima Health. It details the notification procedures, timelines, and actions required for changes like MSO transitions, system updates, and personnel changes. The policy ensures CalOptima Health is informed and can effectively manage these changes."
    },
    {
        'filename': "EE.1124_CEO20241031_v20241001.pdf",
        'title': "Health Network Encounter Data Performance Standards",
        'description': "This policy defines how CalOptima Health measures a Health Network's adherence to encounter data performance standards for services provided to CalOptima Health Medi-Cal members, starting January 1, 2024. It outlines the annual measurement process, the use of scorecards, and potential corrective actions or sanctions for non-compliance."
    },
    {
        'filename': "EE.1135_CEO20241220_v20241201.pdf",
        'title': "Long-Term Care Facilities (LTCFs) Contracting Requirements",
        'description': "This policy outlines CalOptima Health's requirements for contracting with Long-Term Care Facilities (LTCFs), Intermediate Care Facilities, and Skilled Nursing Facilities. It details the processes for establishing contracts and Letter of Agreements (LOAs) to ensure member access to covered services. The policy also addresses contracting with out-of-network facilities when necessary."
    },
    {
        'filename': "EE.1141_20250221.pdf",
        'title': "CalOptima Health Provider Contracts",
        'description': "This policy outlines the process by which CalOptima Health establishes contracts and Letters of Agreement (LOAs) with providers to meet network adequacy and continuity of care obligations. It details provider participation requirements, including Medi-Cal enrollment and exclusion monitoring, as well as the use of provisional LOAs in certain circumstances."
    },
    {
        'filename': "EE.1144_CEO20250227_v20250201.pdf",
        'title': "Memorandum of Understanding (MOU) Requirements for CalOptima Health and Third-Party Entities",
        'description': "This policy establishes the requirements for Memoranda of Understanding (MOUs) between CalOptima Health and Third-Party Entities to ensure coordinated member care and access to resources. It outlines the necessary elements of these MOUs, including clarifying roles, establishing collaboration processes, streamlining referrals, and defining partnerships, in accordance with DHCS guidelines."
    },
    {
        'filename': "EE.1145_CEO20250306_v20250306_final version.pdf",
        'title': "Prospective Health Network",
        'description': "This policy outlines the criteria for adding a new Health Network to CalOptima Health, specifying requirements related to provider network size, risk management, regulatory compliance, and service capabilities. It details the contract models available and emphasizes that approval is not guaranteed and is subject to CalOptima Health's discretion."
    },

    # FF Folder
    {
        'filename': "FF.1001_CEO20240523.pdf",
        'title': "Capitation Payments",
        'description': "This policy outlines the process for CalOptima Health to make timely and accurate capitation payments to health networks. It details how payments are calculated, the factors that influence them, and specific provisions for members eligible for services under the California Children’s Services (CCS) Program, AIDS, and End Stage Renal Disease (ESRD)."
    },
    {
        'filename': "FF.1002_CEO20240620_v20240601.pdf",
        'title': "CalOptima Health Medi-Cal Fee Schedule",
        'description': "This policy outlines the process CalOptima Health uses to establish and maintain its Medi-Cal Fee Schedule. It details how the schedule is updated monthly based on the Department of Health Care Services (DHCS) Fee-for-Service (FFS) Fee Schedule and other DHCS publications. The policy also specifies how reimbursement rates are determined for various services and supplies."
    },
    {
        'filename': "FF.1003_20250221.pdf",
        'title': "Payment for Covered Services Rendered to a Member for which CalOptima Health is Financially Responsible",
        'description': "This policy outlines CalOptima Health's payment methodologies for providers or practitioners that provide covered services to a member for which CalOptima is financially responsible. It specifies rules regarding non-contracted providers, member billing, and overpayment recovery. It also details hospital payment procedures for both contracted and non-contracted hospitals."
    },
    {
        'filename': "FF.1004_CEO20241010_v20241001.pdf",
        'title': "Payment for Hospitals Contracted to\nServe a CalOptima Health Direct\nMember, CalOptima Health\nCommunity Network Member, or a\nMember Enrolled in a Shared Risk\nGroup",
        'description': "This policy defines CalOptima Health Direct reimbursement of contracted hospitals, establishing criteria for tertiary and community hospitals. It applies to reimbursement for members of CalOptima Health Direct, Community Network, or those in a Shared Risk Group within the Medi-Cal Program, specifically for covered services where CalOptima Health is financially responsible."
    },
    {
        'filename': "FF.1005a_v20240404.pdf",
        'title': "Special Payments – Bone\nMarrow Transplant and Major\nOrgan Transplant",
        'description': "This policy outlines CalOptima Health's payment process for covered services related to bone marrow transplants and major organ transplants for Health Network Members, excluding those assigned to Kaiser, when such services are not included in the Health Network's capitation payment. It details the reimbursement process for DHCS-approved transplant centers and CCS-approved special care centers."
    },
    {
        'filename': "FF.1005c_v20240404.pdf",
        'title': "Special Payments: High-Cost Exclusion Items",
        'description': "This policy outlines the process by which CalOptima Health reimburses contracted Fee-For-Service (FFS) hospitals for high-cost exclusion items provided to Medi-Cal members as part of inpatient services paid on a per diem basis. It defines high-cost exclusion items and specifies eligibility and reimbursement conditions for hospitals."
    },
    {
        'filename': "FF.1006_CEO20240808_v20240801.pdf",
        'title': "Financial Risk Arrangements",
        'description': "This policy outlines the process by which CalOptima Health ensures financial risk arrangements, such as Hospital Risk Pool Arrangements, are fair and equitable. It aims to appropriately reward providers for cost-effective, high-quality services to members assigned to a Physician Hospital Consortium (PHC). The policy details requirements for PHCs regarding risk pool establishment, surplus distribution, downside risk limitations, and compliance with relevant laws."
    },
    {
        'filename': "FF.1007_CEO20240509.pdf",
        'title': "Health Network Reinsurance Coverage",
        'description': "This policy outlines CalOptima Health's reinsurance coverage for eligible Health Networks, excluding financially at-risk HMOs, for catastrophic claims. It details the coverage period, eligible claims, and covered expenses for hospital and physician services as defined in the Division of Financial Responsibility (DOFR) between CalOptima Health and the Health Networks."
    },
    {
        'filename': "FF.1009_CEO20240808_v20240801.pdf",
        'title': "Health-based Risk Adjusted\nCapitation Payment System",
        'description': "This policy outlines CalOptima Health's process for a Health-based Risk Adjusted (HRA) Health Network Capitation Payment system. It details how capitation payments are adjusted based on the health status of a Health Network's member population, utilizing the Chronic Illness and Disability Payment System (CDPS). The policy also specifies criteria for member eligibility and risk adjustment categories."
    },
    {
        'filename': "FF.1010_CEO20240523.pdf",
        'title': "Shared Risk Pool",
        'description': "This policy outlines the process for CalOptima Health’s administration of the Shared Risk Pool with a Shared Risk Group. It defines the components of the Shared Risk Budget and Expenses, as well as reporting and reconciliation requirements. The policy also specifies items that are excluded from Shared Risk Expenses."
    },
    {
        'filename': "FF.1014_CEO20250109_v20240901.pdf",
        'title': "Payment for Covered Services Rendered to a Member Enrolled in a Health Network",
        'description': "This policy outlines Health Network payment methodologies for providers offering covered services to members. It details reimbursement procedures for both contracted and non-contracted hospitals, practitioners, and ancillary service providers, specifying rates and conditions. The policy also prohibits providers from billing members directly for covered services."
    },
    {
        'filename': "FF.2001_20250221.pdf",
        'title': "Claims Processing for Covered\nServices for which CalOptima\nHealth is Financially\nResponsible",
        'description': "This policy outlines CalOptima Health's process for ensuring timely and accurate claims processing for covered services for which it is financially responsible. It details compliance with relevant laws, administrative processes, and timelines for claim adjudication and notification. The policy also addresses claim receipt acknowledgement and review for coding accuracy."
    },
    {
        'filename': "FF.2003_v20240404.pdf",
        'title': "Coordination of Benefits",
        'description': "This policy outlines the process for CalOptima Health and its Health Networks to coordinate benefits when a member has Other Health Coverage (OHC), including cost avoidance and post-payment recovery. CalOptima Health will consider OHC plans as primary and will act as the secondary payer of last resort. The policy also details claim adjudication and payment considerations when members have multiple OHC plans or Medicare coverage."
    },
    {
        'filename': "FF.2004_20240404.pdf",
        'title': "Financial Responsibility for\nNewborn Coverage",
        'description': "This policy clarifies the financial responsibility for Covered Services provided to a Newborn whose mother is eligible for Medi-Cal and enrolled in CalOptima Health Direct or a Health Network. It outlines the specific responsibilities of CalOptima Health Direct and Health Networks for newborn care, particularly concerning CCS NICU/PICU services and the period before a Client Index Number (CIN) is assigned to the newborn."
    },
    {
        'filename': "FF.2005_CEO20241122_v20241101.pdf",
        'title': "Conlan, Member Reimbursement",
        'description': "This policy outlines CalOptima Health's process for reimbursing members for out-of-pocket expenses for Medi-Cal covered services, in compliance with the Department of Health Care Services (DHCS) All Plan Letter (APL) 07-002 regarding the Conlan v. Bontá and Conlan v. Shewry court cases. It details eligibility periods, claim submission timelines, and procedures for appeals and recoupment."
    },
    {
        'filename': "FF.2007_CEO20240822_v20240801.pdf",
        'title': "Reporting of Potential Third Party Tort Liability",
        'description': "This policy establishes CalOptima Health’s and a subcontracted Provider’s responsibility for identifying and reporting potential Third Party Tort Liability (TPTL). It outlines procedures for reporting instances where a Medi-Cal member's action involving casualty insurance, tort, or Workers’ Compensation could result in a recovery of funds to which the Department of Health Care Services (DHCS) has lien rights. The policy also addresses the process of handling requests for service information or bills related to potential TPTL cases."
    },
    {
        'filename': "FF.2009_CEO20240808_v20240801.pdf",
        'title': "Mailing of Provider Checks",
        'description': "This policy outlines the procedures for mailing provider checks, ensuring timely payments. It specifies different processes based on the check amount, with amounts over $25,000 requiring a second signature. The policy also dictates the frequency of check printing and mailing by CalOptima Health's third-party vendor."
    },
    {
        'filename': "FF.2011_CEO20240808_v20240701.pdf",
        'title': "Directed Payments for\nQualifying Services Rendered to\nCalOptima Health, Health\nNetwork Members When Health\nNetworks are Financially\nResponsible for the Qualifying\nServices",
        'description': "This policy establishes requirements for Health Networks to administer Directed Payments for Qualifying Services and outlines the reimbursement processes between CalOptima Health and the Health Networks, as well as between Health Networks and their Designated Providers. It details the conditions under which a Health Network qualifies for reimbursement of these Directed Payments and specifies the Qualifying Services eligible for such payments."
    },
    {
        'filename': "FF.2012_CEO20240808_v20240701.pdf",
        'title': "Directed Payments for\nQualifying Services Rendered to\nCalOptima Health Direct\nMembers or to Shared Risk\nGroup Members When\nCalOptima Health is Financially\nResponsible for the Qualifying\nServices",
        'description': "This policy outlines the requirements for CalOptima Health to administer directed payments for qualifying services rendered to CalOptima Health Direct or Shared Risk Group members. It specifies the conditions under which a designated provider qualifies for reimbursement, including eligibility, enrollment, and service dates. For Shared Risk Group Members, only Ground Emergency Medical Transport (GEMT) Services are eligible for Directed Payments when CalOptima Health is financially responsible."
    },
    {
        'filename': "FF.3001_CEO20240808_v20240801.pdf",
        'title': "Financial Reporting",
        'description': "This policy outlines the process by which CalOptima Health monitors the timely submission of required financial reports by Health Networks. It details the types of reports required, submission deadlines, and the manner in which they should be submitted to ensure financial viability and stability of Health Networks."
    },
    {
        'filename': "FF.3002_CEO20240808_v20240801.pdf",
        'title': "Financial Oversight",
        'description': "This policy outlines the process by which CalOptima monitors a Health Network’s financial position and financial security reserves to ensure contract compliance and financial integrity. It also details the financial solvency reserve requirements that Health Networks must comply with, including financial security reserves and capitation payment withholds. CalOptima Health may adjust these requirements based on its assessment of the operational readiness and financial condition of the Health Network."
    },
    {
        'filename': "FF.3003_CEO20241220_v20241201.pdf",
        'title': "Minimum Medical Loss Ratio",
        'description': "This policy defines the minimum acceptable Medical Loss Ratio (MLR) for Health Networks participating with CalOptima Health, as required by the Department of Health Care Services (DHCS) for Medi-Cal Managed Care Plan's Subcontractors and Downstream Subcontractors. It outlines the MLR requirements, reporting responsibilities, and potential penalties for non-compliance."
    },
    {
        'filename': "FF.4000_CEO20240620_v20240601.pdf",
        'title': "Whole-Child Model – Financial Reimbursement for Capitated Health Networks",
        'description': "This policy outlines the reimbursement process CalOptima Health uses to distribute Whole-Child Model (WCM) payments to Health Networks for services provided to California Children’s Services (CCS) Program-eligible members. It details the payment methodology, including capitation payments, catastrophic payments, and risk corridor settlements, and specifies timelines for payment and reconciliation."
    },
    {
        'filename': "FF.4002_CEO20240808_v20240801.pdf",
        'title': "Special Payments: Enhanced Care Management Supplemental Payment",
        'description': "This policy outlines the criteria for Enhanced Care Management (ECM) Providers to receive supplemental payments for ECM services provided to eligible members, including outreach to specific populations. It details the conditions that must be met for CalOptima Health to issue these payments and specifies circumstances under which payments may be recovered."
    },

    # GA Folder
    {
        'filename': "GA.8048_CEO20250129_v20241231.pdf",
        'title': "Restrictions on Smoking and\nUnregulated Nicotine Products",
        'description': "This policy defines and establishes CalOptima Health’s restrictions on smoking and the use of unregulated nicotine products in or on property owned, operated, or leased by CalOptima Health. Smoking and the use of unregulated nicotine products are strictly prohibited inside and outside of CalOptima Health property, except in designated outside smoking areas at least 25 feet away from buildings, with the PACE center not allowing it anywhere on the property."
    },
    {
        'filename': "GA.7107_CEO20250129_v20241231.pdf",
        'title': "Mail Collection and Delivery",
        'description': "This policy outlines the process for collecting and delivering mail for CalOptima Health. It establishes procedures to ensure that all incoming and outgoing mail is documented and processed in a cost-effective and timely manner. The policy also defines mailroom hours and procedures for after-hours mail handling."
    },
    {
        'filename': "GA.4010_CEO20241220_v20241201.pdf",
        'title': "Service Animals",
        'description': "This policy outlines CalOptima Health's guidelines for allowing individuals with disabilities to bring service animals onto CalOptima Health property. It details where service animals are permitted, requirements for their control, and considerations for accommodation, while also ensuring non-discrimination against individuals using service animals."
    },
    {
        'filename': "GA.7111_CEO20240725_v2024070.pdf",
        'title': "Health Network Certification Process",
        'description': "This policy outlines the requirements for delegating and monitoring Health Networks, detailing the Subcontractor Network Certification (SNC) process. It aims to ensure CalOptima Health's Health Networks and delegates meet state and federal network adequacy and access requirements, including SNC document submission."
    },
    {
        'filename': "GA.7110_v20240201_CEO20240222_no attachments.pdf",
        'title': "Street Medicine",
        'description': "This policy outlines CalOptima Health's and provider responsibilities for administering and implementing a Street Medicine program, which provides medical services to members experiencing unsheltered homelessness, as required by the California Department of Health Care Services (DHCS). It details provider eligibility, reimbursement guidelines, and the option for Street Medicine Providers to serve as Primary Care Providers (PCPs)."
    },

    # GG Folder
    {
        'filename': "GG.1100_CEO20250129_v20241231.pdf",
        'title': "Alcohol and Substance Use Disorder Treatment Services",
        'description': "This policy outlines the process for Medi-Cal members to access medically necessary alcohol and substance use disorder treatment services. It specifies which services are covered under the CalOptima Health Medi-Cal program, focusing on screening, brief interventions, and referral to treatment (SBIRT) for specific age groups and circumstances."
    },
    {
        'filename': "GG.1101_CEO20250227_v20250101.pdf",
        'title': "California Children’s Services (CCS)/Whole-Child Model – Coordination with County CCS Program",
        'description': "This policy outlines the guidelines for coordination of care between CalOptima Health or a Health Network and the County California Children’s Services (CCS) program. It defines responsibilities for managing CCS-eligible members, ensuring continuity of care, and complying with relevant regulations and guidelines related to the Whole Child Model (WCM) program. CalOptima Health is also required to establish agreements with County CCS programs and conduct regular meetings for service coordination."
    },
    {
        'filename': "GG.1102_v20231231_CEO20240129_no attachments.pdf",
        'title': "Experimental and\nInvestigational Service Coverage",
        'description': "This policy defines the benefit coverage for Experimental and Investigational Services under the CalOptima Health program. It outlines specific conditions for coverage of investigational services in Medi-Cal and OneCare programs, while generally excluding experimental services under DHCS Medi-Cal, WCM, and CMS Medicare or Duals Demonstration programs unless specified by law."
    },
    {
        'filename': "GG.1103_CEO20241220_v20241201.pdf",
        'title': "Specialty Mental Health Services",
        'description': "This policy outlines the responsibilities of CalOptima Health and Health Networks regarding Specialty Mental Health Services (SMHS) managed by the Orange County Health Care Agency (OCHCA) for Medi-Cal and OneCare members. It clarifies that OCHCA is responsible for providing SMHS, while CalOptima Health is responsible for coordinating and paying for related physical health services and transportation."
    },
    {
        'filename': "GG.1105_CEO20240509.pdf",
        'title': "Coverage of Organ and Tissue\nTransplants",
        'description': "This policy defines transplant coverage for CalOptima Health Members under the Medi-Cal program. It outlines which transplants are covered, the criteria for patient selection, and requirements for Centers of Excellence.  It also addresses case management related to transplant services."
    },
    {
        'filename': "GG.1107_CEO20241220_v20241201.pdf",
        'title': "Coverage for Members\nTransitioning between\nCalOptima Health and a Health\nNetwork or between Health\nNetworks, including CalOptima\nHealth Community Network",
        'description': "This policy clarifies responsibility for healthcare coverage during transitions between CalOptima Health, Health Networks, and CalOptima Health Community Network (CHCN). It outlines which entity is responsible for coverage at different stages of enrollment and during transitions, including continuity of care and durable medical equipment."
    },
    {
        'filename': "GG.1109_CEO20241220_v20241201.pdf",
        'title': "CalOptima Health and Health Network Newborn and Prenatal Genetic Screening Services",
        'description': "This policy outlines the requirements for newborn and prenatal genetic screening services for CalOptima Health and Health Network members, as mandated by state law. It covers prenatal blood testing, member participation, diagnostic amniocentesis, and Practitioner responsibilities related to screening programs and reporting requirements. The policy aims to ensure timely and effective genetic disease prevention, early detection, diagnosis, treatment, education, and counseling."
    },
    {
        'filename': "GG.1110_CEO20241031_v20241001.pdf",
        'title': "Primary Care Practitioner\nDefinition, Role, and\nResponsibilities",
        'description': "This policy defines the role and responsibilities of Primary Care Practitioners (PCPs) in providing Covered Services and Case Management to Members within the CalOptima Health network. It outlines requirements for PCPs, including enrollment, credentialing, and the scope of services they must provide. The policy also details PCP responsibilities related to member eligibility verification, care coordination, and referral processes."
    },
    {
        'filename': "GG.1111_CEO20241220_v20241201.pdf",
        'title': "Vision Services",
        'description': "This policy outlines the provision of vision services to CalOptima Health members, detailing coverage for services like optical frames, plastic and polycarbonate lenses, and the roles of Vision Services Plan (VSP) providers and Health Networks. It specifies conditions for coverage, referral processes, and financial responsibilities related to vision care."
    },
    {
        'filename': "GG.1112_CEO20241220_v20241201.pdf",
        'title': "Standing Referral to Specialty Care Provider or Specialty Care Center",
        'description': "This policy defines the conditions under which CalOptima Health and its Health Networks shall authorize a Standing Referral to a Specialty Care Provider or a Specialty Care Center. It outlines the circumstances under which a standing referral may be authorized, including requirements for treatment of life-threatening, degenerative, or disabling conditions, and the process for requesting and approving such referrals."
    },
    {
        'filename': "GG.1113_CEO20241220_v20241201.pdf",
        'title': "Specialty Practitioner Responsibilities",
        'description': "This policy outlines the responsibilities of a Specialty Practitioner for CalOptima Health Members, including referral processes, authorization requirements, and reporting obligations to the Member's Primary Care Practitioner. It also addresses billing practices and credentialing requirements for contracted Specialty Care Practitioners."
    },
    {
        'filename': "GG.1114_v20240101_CEO20231214_no attachments.pdf",
        'title': "Authorization for Disposable Incontinence Supplies",
        'description': "This policy outlines the coverage and authorization guidelines for disposable incontinence supplies within the CalOptima Health program. It details requirements for prior authorization, restrictions in long-term care facilities, authorization periods, and the use of contracted vendors for obtaining these supplies."
    },
    {
        'filename': "GG.1116_CEO20241122_v20241101.pdf",
        'title': "Pediatric Preventive Services",
        'description': "This policy outlines CalOptima Health's process for ensuring that members under 21 receive Pediatric Preventive Services, in accordance with contract requirements, state, and federal regulations. It details the services included, such as initial health appointments, CHDP services, routine preventive visits, screenings, and vaccinations, and emphasizes adherence to established guidelines and protocols."
    },
    {
        'filename': "GG.1118_CEO20240725_v20240701.pdf",
        'title': "Family Planning Services, Out-of-Network",
        'description': "This policy outlines CalOptima Health's process for ensuring members can access family planning services from any qualified provider, including out-of-network practitioners, without prior authorization. It also details state-allowed limitations on reimbursement to out-of-network practitioners and addresses minor consent and confidentiality requirements related to these services."
    },
    {
        'filename': "GG.1119_CEO20241220_20241201.pdf",
        'title': "Direct Access to OB/GYN Practitioner Service",
        'description': "This policy outlines the standards for female members to self-refer to Obstetrics/Gynecology (OB/GYN) practitioners for routine and preventative healthcare without needing a referral from their Primary Care Physician (PCP) or prior authorization. It also specifies requirements for OB/GYN practitioners, including communication with the member's PCP and ensuring timely prenatal visits."
    },
    {
        'filename': "GG.1120_CEO20241220_v20241201.pdf",
        'title': "Inpatient Length of Stay for Obstetrical Delivery",
        'description': "This policy defines the standard length of stay for members admitted for obstetrical delivery, in compliance with state and federal guidelines. It specifies minimum inpatient hospital stay durations following vaginal and cesarean deliveries and outlines authorization requirements for continued hospitalization beyond those periods."
    },
    {
        'filename': "GG.1121_CEO20240509_no attachments.pdf",
        'title': "Early and Periodic Screening, Diagnosis and Treatment (EPSDT) Services",
        'description': "This policy defines the scope, promotion, and responsibilities for providing Early and Periodic Screening, Diagnosis, and Treatment (EPSDT) services within CalOptima Health's Covered Services. It outlines the requirements for CalOptima Health and its Health Networks to provide appropriate preventive, mental health, developmental, and specialty EPSDT medical services to eligible children under 21 years of age, ensuring access to medically necessary services and compliance with relevant guidelines and regulations."
    },
    {
        'filename': "GG.1122_CEO20241220_v20241201.pdf",
        'title': "Follow-Up for Emergency Department Care",
        'description': "This policy outlines the standard process for ensuring that providers, including delegated Health Networks, coordinate follow-up care for members who receive emergency department services and require further attention. It establishes requirements for Health Networks and PCPs to arrange appropriate follow-up care and monitor coordination of services, including education on appropriate healthcare utilization."
    },
    {
        'filename': "GG.1125_CEO20241220_v20241201.pdf",
        'title': "Clinical Trials",
        'description': "This policy establishes coverage guidelines for routine health care services provided in connection with a Member’s participation in a Clinical Trial. It defines what constitutes routine patient care costs and outlines eligibility requirements for coverage of these costs when participating in a clinical trial."
    },
    {
        'filename': "GG.1128_CEO20241220_v20241201.pdf",
        'title': "Tuberculosis Services",
        'description': "This policy defines the responsibility of CalOptima Health and its Health Networks in providing Tuberculosis (TB) Services to members, including screening, diagnosis, treatment, case management, and follow-up care. It also outlines collaboration with the Orange County Health Care Agency/Pulmonary Disease Services (HCA/PDS) and reporting requirements for active TB cases."
    },
    {
        'filename': "GG.1130_CEO20240515.pdf",
        'title': "Community Based Adult Services (CBAS) Eligibility, Authorization, Availability, and Care Coordination Processes",
        'description': "This policy defines the coverage, eligibility, authorization, availability, and care coordination processes for members enrolled in the Community-Based Adult Services (CBAS) Program. It outlines the eligibility and medical necessity criteria that members must meet to qualify for CBAS, including requirements related to age, program enrollment, and level of care needs."
    },
    {
        'filename': "GG.1132_CEO20240509_QA.pdf",
        'title': "Medi-Cal Annual Wellness Visit",
        'description': "This policy outlines the program to promote and document Annual Wellness Visits (AWV) for adult Medi-Cal members who are 45 years or older, excluding dual eligible members. It describes the components of the Medi-Cal AWV program, including incentives for both members and qualified providers for completing and providing comprehensive AWVs."
    },
    {
        'filename': "GG.1201_CEO20241113_v20241001.pdf",
        'title': "Health Education Programs",
        'description': "This policy establishes standards for health education programs available to CalOptima Health members. It outlines the requirements for maintaining a health education system that provides organized programs, services, and education to assist members in improving their health and managing illness, while addressing health disparities and meeting NCQA requirements."
    },
    {
        'filename': "GG.1204_CEO20250306_v20250301.pdf",
        'title': "Clinical Practice Guidelines",
        'description': "This policy outlines CalOptima Health's process for adopting, disseminating, and monitoring Clinical Practice Guidelines (CPGs) relevant to members for preventive, acute, chronic medical, and behavioral health services. It ensures practitioners use relevant CPGs and establishes guidelines based on valid clinical evidence or consensus among healthcare professionals. The policy also covers distribution of guidelines and their review by the Quality Improvement Health Equity Committee (QIHEC)."
    },
    {
        'filename': "GG.1205_CEO20241010_v20241001.pdf",
        'title': "HEDIS® Data Collection and Reporting",
        'description': "This policy outlines the process for Health Plan Effectiveness Data & Information Set (HEDIS®) reporting at CalOptima Health. It details the data collection, audit preparation, and reporting procedures necessary to meet requirements from the Department of Health Care Services (DHCS) and the Centers for Medicare & Medicaid Services (CMS), ensuring the organization maintains National Committee for Quality Assurance (NCQA) health plan accreditation."
    },
    {
        'filename': "GG.1206_CEO20241031_v20241001.pdf",
        'title': "Readability and Suitability of Written Health Education Materials",
        'description': "This policy defines the review and approval process for the readability and suitability of all written Member Health Education Materials, aligning with guidelines from the California Department of Health Care Services (DHCS) and the Centers for Medicare & Medicaid Services (CMS). It ensures that CalOptima Health provides organized programs and resources to deliver health education and promote positive health outcomes for its members. A Qualified Health Educator must approve all written Member Health Education Materials utilizing the Readability and Suitability Checklist."
    },
    {
        'filename': "GG.1211_CEO20241031_v20241001.pdf",
        'title': "Health Appraisals and Self-Management Tools",
        'description': "This policy establishes a process for Members to manage their health through Health Appraisals and Self-Management Tools. CalOptima Health is required to offer a Health Appraisal to Adult Members annually to determine risk factors and recommend ways to improve or maintain health. The policy also outlines requirements for member information confidentiality and accessibility of documents in threshold languages."
    },
    {
        'filename': "GG.1213_CEO20250116_v20250101.pdf",
        'title': "Community Health Worker Services",
        'description': "This policy outlines the eligibility criteria for CalOptima Health Community Health Worker (CHW) Services and specifies the qualifications required for CHW providers and the provision of CHW services as a benefit. It details the types of preventive health services CHWs deliver and the areas in which they can assist members, including chronic conditions, behavioral health, and preventive care."
    },
    {
        'filename': "GG.1301_v20230701_CEO20231220_no attachments.pdf",
        'title': "Comprehensive Care Management Process",
        'description': "This policy outlines the guidelines for Case Management of Medi-Cal members enrolled by CalOptima Health or a Health Network. It focuses on Complex Case Management, which coordinates care for members with critical events or diagnoses requiring extensive resources, aiming to improve health and functional capability in a cost-effective manner. The policy details assessment, evaluation, and individualized care plan development for members."
    },
    {
        'filename': "GG.1302a_v20231001_CEO20231102_no attachments.pdf",
        'title': "Coordination of Care for\nRegional Center of Orange\nCounty (RCOC) Members",
        'description': "This policy outlines the guidelines for CalOptima Health or its Health Networks to coordinate care for members eligible for services from the Regional Center of Orange County (RCOC). It covers identification, referral, and provision of services in accordance with the Memorandum of Understanding between CalOptima Health and RCOC, as well as relevant CalOptima Health policies."
    },
    {
        'filename': "GG.1304_CEO20250129_v20250101.pdf",
        'title': "Continuity of Care During Health Network or Provider Termination",
        'description': "This policy establishes guidelines for coverage and continuity of care when a member is involuntarily required to change Health Networks or Providers. It ensures a safe transition and uninterrupted access to covered services during provider terminations or non-renewals. The policy outlines responsibilities for CalOptima Health and Health Networks in coordinating care and notifying members of changes."
    },
    {
        'filename': "GG.1308_v20240101_CEO20231214_no attachments.pdf",
        'title': "Monitoring Health Network Compliance via Case Management Reports",
        'description': "This policy outlines CalOptima Health’s process for monitoring Health Network compliance through monthly Case Management reports. It details the requirements for Health Networks to submit monthly Case Management Logs and the procedures CalOptima Health will use to review and monitor these reports for compliance. The policy also covers data exchange with Health Networks to facilitate care coordination, ensuring compliance with HIPAA and other relevant regulations."
    },
    {
        'filename': "GG.1312_CEO20241220_v20241201.pdf",
        'title': "Responsibility for a Member in\na State Hospital",
        'description': "This policy defines the division of financial responsibility and coordination of care for a CalOptima Health member who resides in a State Hospital. It outlines which services CalOptima Health or the Health Network is responsible for, both within and outside of the State Hospital, including emergency and elective medical treatments. The policy also details procedures for emergency and elective services, including authorization and transportation responsibilities."
    },
    {
        'filename': "GG.1313_CEO20250129_v20250101.pdf",
        'title': "Coordination of Care for\nTransplant Members",
        'description': "This policy defines the Case Management guidelines for Care Coordination by CalOptima Health and a Health Network for members who are candidates for a transplant. It outlines the responsibilities of CalOptima Health and the Health Network during the referral, evaluation, transplant, and post-transplant phases. The policy also ensures continuity of care for members transitioning into CalOptima Health Services while undergoing transplant-related procedures."
    },
    {
        'filename': "GG.1317_CEO20241220_v20241201.pdf",
        'title': "Response to Disruptive and\nThreatening Behavior by\nMembers",
        'description': "This policy outlines CalOptima Health and its Health Networks’ process for responding to disruptive and threatening behavior by a Member. It defines disruptive and threatening behaviors and describes actions CalOptima Health and its Health Networks shall take in response."
    },
    {
        'filename': "GG.1318_v20240101_CEO20231214_no attachments.pdf",
        'title': "Coordination of Care for\nHemophilia Members",
        'description': "This policy defines the case management guidelines for coordination of care by CalOptima Health and its Health Networks for Members diagnosed with Hemophilia. It outlines the responsibilities of CalOptima Health and Health Networks in managing and transitioning members with Hemophilia to CalOptima Health Direct, ensuring they receive care from a Federal Hemophilia Treatment Center and Hemophilia factor from a 340B Drug Pricing Program registered pharmacy."
    },
    {
        'filename': "GG.1320_v20231201_CEO20231226.pdf",
        'title': "Elder or Dependent Adult Abuse Reporting",
        'description': "This policy outlines CalOptima Health's process for reporting known or suspected elder or dependent adult abuse, as mandated by California law. It details the responsibilities of mandated reporters, including reporting procedures and confidentiality requirements, and ensures CalOptima Health provides adequate training and support for these reporters."
    },
    {
        'filename': "GG.1321_v20240404.pdf",
        'title': "Coordination of Care for Local Education Agency Services",
        'description': "This policy outlines the guidelines for care coordination between CalOptima Health or a Health Network and Local Education Agencies (LEAs) for members eligible for LEA services. It defines the roles and responsibilities of each entity in ensuring members receive medically necessary services, particularly those identified in Individualized Education Plans (IEPs) or Individual Family Service Plans (IFSPs). CalOptima Health is not responsible for LEA service costs except where specified."
    },
    {
        'filename': "GG.1323_v20230401_CEO20230823_no attachments_.pdf",
        'title': "Seniors and Persons with\nDisabilities and Health Risk\nAssessment",
        'description': "This policy outlines the process for identifying the health risk of Medi-Cal Seniors and Persons with Disabilities (SPD) members. It details how CalOptima Health uses a risk stratification algorithm and Health Risk Assessment (HRA) to develop individualized care plans for these members through case management."
    },
    {
        'filename': "GG.1324_v20230301_CEO20230823_no attachments.pdf",
        'title': "Seniors and Persons with\nDisabilities (SPD)\nComprehensive Case\nManagement",
        'description': "This policy outlines the guidelines for providing Comprehensive Medical Case Management to CalOptima Health Seniors and Persons with Disabilities (SPD). It details the coordination of care services for high-risk SPD members, emphasizing a systematic process for identifying members who would benefit from these services and the implementation of Individual Care Plans."
    },
    {
        'filename': "GG.1325_CEO20250306_v20250301.pdf",
        'title': "Continuity of Care for Members Transitioning into CalOptima",
        'description': "This policy outlines the guidelines and processes for ensuring continuity of care for newly enrolled Medi-Cal members transitioning into CalOptima Health, or existing members whose covered services are transitioned from Medi-Cal Fee-for-Service to CalOptima Health. It covers screening for expedited services, making screening results available upon disenrollment, and providing continuity of care for up to 12 months for eligible members."
    },
    {
        'filename': "GG.1330_CEO20250227_v20250101.pdf",
        'title': "Case Management - California Children’s Services Program/Whole-Child Model",
        'description': "This policy outlines the guidelines for Case Management provided by CalOptima Health or a Health Network to eligible CalOptima Health Members within the California Children’s Services (CCS) program or the Whole-Child Model (WCM) program. It details responsibilities for authorization, payment of CCS-eligible services, and care coordination, ensuring staff have adequate training on the CCS program and clinical experience with pediatric patients."
    },
    {
        'filename': "GG.1352_v20231101_CEO20231207_no attachments.pdf",
        'title': "Private Duty Nursing Care Management",
        'description': "This policy defines the scope of case management services for Private Duty Nursing (PDN) for CalOptima Health Medi-Cal members under 21. It outlines the responsibilities of CalOptima Health and its Health Networks in providing and coordinating these services, including case management, for eligible members."
    },
    {
        'filename': "GG.1353_CEO20240905_v20240801.pdf",
        'title': "CalAIM Enhanced Care Management Service Delivery",
        'description': "This policy outlines the process for providing Enhanced Care Management (ECM) under the California Advancing and Innovating Medi-Cal for All (CalAIM) initiative. It details the responsibilities of ECM providers, including outreach, care coordination, and ensuring access to core services for eligible members. The policy also covers eligibility determination and oversight of ECM providers."
    },
    {
        'filename': "GG.1354_CEO20240905_v20240801.pdf",
        'title': "CalAIM Enhanced Care Management - Eligibility and Outreach",
        'description': "This policy outlines the implementation of Enhanced Care Management (ECM) under the CalAIM initiative. It details the processes for identifying eligible Medi-Cal members and conducting outreach activities for Populations of Focus (POF). The policy describes the phased implementation of ECM for various groups, including individuals experiencing homelessness, those at risk for avoidable hospitalizations, and children/youth with serious mental health needs."
    },
    {
        'filename': "GG.1355_CEO20240924_v20240901.pdf",
        'title': "CalAIM Community Supports",
        'description': "This policy outlines the eligibility criteria, referral process, authorization, and provision requirements for CalOptima Health Community Supports under the California Advancing and Innovating Medi-Cal (CalAIM) initiative. It details the specific DHCS-approved Community Supports offered by CalOptima Health, with varying effective dates, and emphasizes that participation is optional for members and should not reduce access to state plan services."
    },
    {
        'filename': "GG.1356_CEO20240905_v20240801.pdf",
        'title': "CalAIM Enhanced Care Management Administration",
        'description': "This policy outlines CalOptima Health's responsibilities for administering Enhanced Care Management (ECM) under the CalAIM initiative. It details the phased implementation of ECM for Populations of Focus (POF), the selection of ECM providers, and the authorization of ECM services. The policy also addresses continuity of care during Medi-Cal Managed Care Plan transitions."
    },
    {
        'filename': "GG.1357_CEO20240918_v20240901.pdf",
        'title': "Population Health Management\nTransitional Care Services\n(TCS)",
        'description': "This policy defines CalOptima Health’s Transitional Care Services (TCS) and describes the process by which CalOptima Health, Health Networks, and Providers engage Members across all settings and delivery systems. It ensures Members are supported from discharge planning until they have been successfully connected to all needed services and supports."
    },
    {
        'filename': "GG.1401_CEO20240509_no attachments.pdf",
        'title': "Physician Administered Drug (PAD) Prior Authorization Process",
        'description': "This policy outlines CalOptima Health's process for Prior Authorization (PA) of Physician Administered Drugs (PAD). It details requirements for PAs, communication protocols with providers and members, and timelines for decisions, including expedited requests and those for terminally ill patients."
    },
    {
        'filename': "GG.1407_CEO20241216_v20241201.pdf",
        'title': "Nutrition Products",
        'description': "This policy defines the scope of coverage for nutrition products on an outpatient basis for CalOptima Health members. It outlines which nutrition products are covered and not covered under Medi-Cal, as well as the criteria for prior authorization, including specific requirements for different types of nutritional products."
    },
    {
        'filename': "GG.1409_CEO20241031_v20241001.pdf",
        'title': "Physician Administered Drug\nPrior Authorization Required\nList Development and\nManagement",
        'description': "This policy defines CalOptima Health's process for developing and managing the Physician Administered Drug Prior Authorization required List (PAD PA List). The policy ensures member access to clinically appropriate and cost-effective pharmaceuticals, according to the Pharmacy and Therapeutics (P&T) Committee's decisions and consistent with pharmaceutical service benefits established by the California Department of Health Care Services (DHCS)."
    },
    {
        'filename': "GG.1422_CEO20241031_v20241001.pdf",
        'title': "Notification Regarding Medication Recalls",
        'description': "This policy outlines CalOptima Health's process for notifying members and prescribers about medication recalls and market withdrawals. It details the monitoring of FDA reports, the notification procedures for different recall classes, and the timeline for identifying and informing affected parties."
    },
    {
        'filename': "GG.1428_v20240301_CEO20240328_no attachments.pdf",
        'title': "Pharmacy Management Medi-Cal Rx Responsibilities",
        'description': "This policy outlines CalOptima Health's responsibilities for pharmacy management under the Medi-Cal Rx program, including providing information to the Department of Health Care Services (DHCS) on policies regarding clinical aspects of pharmacy adherence and retrospective drug utilization review (DUR) services. It details participation in a global Medi-Cal DUR program and adherence to specific guidelines and monitoring processes to ensure appropriate and safe drug utilization."
    },
    {
    'filename': "GG.1500_CEO20241122_v20241101.pdf",
    'title': "Authorization Instructions for\nCalOptima Health Direct and\nCalOptima Health Community\nNetwork Providers",
    'description': "This policy defines the authorization process for Covered Services for CalOptima Health Direct (COHD) or CalOptima Health Community Network (CHCN) Members, including Prior Authorization, Concurrent Review, and Retrospective Review. It outlines when and how providers should request authorization for services, including timelines for retrospective authorization requests and considerations for members with Other Health Coverage or retroactive eligibility."
    },
    {
        'filename': "GG.1501_CEO20240605_v20240601.pdf",
        'title': "Inpatient Length of Stay (LOS)",
        'description': "This policy outlines the procedure and guidelines for assigning inpatient Length of Stay (LOS) for CalOptima Health Members. The Utilization Management (UM) Department assigns an authorized inpatient admission and LOS based on Medical Necessity and nationally recognized, evidence-based criteria. Hospitals and Skilled Nursing Facilities (SNF) are required to notify CalOptima Health within 24 hours of an inpatient admission."
    },
    {
        'filename': "GG.1502_CEO20240523.pdf",
        'title': "Criteria and Authorization\nProcess for Durable Medical\nEquipment (DME), Excluding\nWheelchairs",
        'description': "This policy defines the criteria and process for coverage of Durable Medical Equipment (DME) for CalOptima Health members, excluding wheelchairs. It outlines what DME is considered a covered service and lists items that are not covered, along with conditions for authorization, including the use of Augmentation and Alternative Communication (AAC) devices."
    },
    {
        'filename': "GG.1503_CEO20240924_v20240901.pdf",
        'title': "CalOptima Health Hospice Coverage, Notification and Validation Requirements",
        'description': "This policy clarifies CalOptima Health's hospice benefit coverage, notification, and validation requirements for members enrolled in Medi-Cal, OneCare, PACE, or Administrative programs. It outlines eligibility requirements for both Medicare and Medi-Cal hospice benefits and defines the responsibilities of CalOptima Health and its Health Networks in providing Hospice Care services."
    },
    {
        'filename': "GG.1504_v20240410.pdf",
        'title': "Dental Services",
        'description': "This policy outlines CalOptima Health's coverage responsibilities related to anesthesia services provided in conjunction with dental services for its members. It specifies the settings where members can receive treatment under sedation or anesthesia and the conditions under which CalOptima Health will reimburse facility fees and anesthesia services."
    },
    {
        'filename': "GG.1505_CEO20240523.pdf",
        'title': "Transportation: Emergency,\nNon-Emergency, and Non-\nMedical",
        'description': "This policy outlines the coverage and authorization requirements for Emergency, Non-Emergency, and Non-Medical Transportation services for CalOptima Health Members. It details the conditions under which different modes of transportation (ambulance, litter van, wheelchair van, air) are covered, including specific regulations and guidelines from Title 22, California Code of Regulations, and the Medi-Cal Provider Manual."
    },
    {
        'filename': "GG.1506_CEO20241220_v20241201.pdf",
        'title': "Guidelines for Advance\nDirectives for CalOptima Health\nMembers",
        'description': "This policy defines CalOptima Health’s responsibility to provide Advance Directive information to CalOptima Health Members. It outlines the process for informing members about their right to make medical care decisions and providing them with resources related to Advance Directives. Completion of an Advance Directive is not a requirement for receiving services."
    },
    {
        'filename': "GG.1507_CEO20240515.pdf",
        'title': "Notification Requirements for\nCovered Services Requiring\nPrior Authorization",
        'description': "This policy outlines CalOptima Health's guidelines for notifying members, their representatives, prescribing practitioners, and PCPs when a prior authorization request for a covered service is processed, denied, modified, or delayed. It also addresses the requirements for providing adequate notice before denying, reducing, suspending, or terminating services, especially for members with visual impairments or other disabilities."
    },
    {
        'filename': "GG.1508_CEO20241122_v20241101.pdf",
        'title': "Authorization and Processing of\nReferrals",
        'description': "This policy outlines the procedure by which CalOptima Health and its Health Networks will process requests for Prior Authorization, Concurrent Review, and Retrospective Review of Covered Services for members. It also details the timeframes for decisions and notifications related to these requests and emphasizes that clinical decisions must be based on sound medical evidence."
    },
    {
        'filename': "GG.1510_20250214.pdf",
        'title': "Member Appeal Process",
        'description': "This policy outlines the process by which CalOptima Health handles member appeals of adverse benefit determinations, including denials or modifications of services based on medical necessity. It details the procedures for standard and expedited appeals, member rights, and timeframes for resolution, ensuring compliance with applicable regulations."
    },
    {
        'filename': "GG.1513_CEO20241220_20241201.pdf",
        'title': "Health Network Utilization Management Reporting and Monitoring Requirements",
        'description': "This policy defines the Utilization Management (UM) reporting requirements for Health Networks and the process for monitoring these reports. It outlines what information Health Networks must submit to CalOptima Health regarding UM activities and how CalOptima Health will review and monitor these reports for compliance and potential over/underutilization."
    },
    {
        'filename': "GG.1515_CEO20240523.pdf",
        'title': "Criteria for Medically Necessary\n` Automobile Orthopedic\nPositioning Devices",
        'description': "This policy defines the Durable Medical Equipment (DME) guidelines and Medical Necessity criteria for reimbursement of Medically Necessary Automobile Orthopedic Positioning Devices (AOPD) provided to Members. It outlines the conditions under which an AOPD is a Covered Service and requires Prior Authorization for purchase and reimbursement. The policy specifies that CalOptima Health will review for Medical Necessity and authorize the purchase of AOPDs for children with medical conditions requiring specially adapted devices."
    },
    {
        'filename': "GG.1516_CEO20250129_v20241231.pdf",
        'title': "Hospital Acute Administrative Days",
        'description': "This policy defines the criteria for authorizing Acute Administrative Days for CalOptima Health Direct Members. It outlines the conditions under which such days are approved, including when a member no longer requires acute hospital care but needs a transition to a skilled nursing facility or similar setting, or in specific cases like pregnant members or those with tuberculosis. The policy also details the facility's responsibilities regarding placement efforts."
    },
    {
        'filename': "GG.1517_CEO20240523.pdf",
        'title': "Transgender Services",
        'description': "This policy defines the provision of covered, Medically Necessary Transgender Services to Medi-Cal and OneCare Members. It outlines the process for determining medical necessity and reconstructive surgery, ensuring non-discrimination based on gender identity or expression, and adhering to nationally recognized medical guidelines."
    },
    {
        'filename': "GG.1531_CEO20240605_v20240601.pdf",
        'title': "Criteria and Authorization Process for Wheelchair Rental, Purchase, and Repair",
        'description': "This policy defines the criteria and process for coverage of wheelchairs, seating and positioning components (SPCs), and accessories for CalOptima Health members. It outlines what is considered medically necessary and what types of wheelchairs and accessories are covered, as well as items that are not covered services."
    },
    {
        'filename': "GG.1532_CEO20250129_v20241231.pdf",
        'title': "Over and Under Utilization\nMonitoring",
        'description': "This policy outlines the process for CalOptima Health to track and trend the appropriate utilization of medical care and services delivered to Members. It ensures that care is monitored, analyzed, and interventions are implemented upon the identification of under and/or over utilization patterns. The Utilization Management Committee (UMC) reviews benchmarks to monitor service utilization."
    },
    {
        'filename': "GG.1535_CEO20241220_v20241201.pdf",
        'title': "Utilization Review Criteria and\nGuidelines",
        'description': "This policy defines the process by which CalOptima Health establishes utilization criteria and guidelines to ensure consistent organization determination decisions related to utilization management. It emphasizes that UM decisions are based on appropriateness of care and coverage, and not on rewarding practitioners for denying care. The policy also mandates that criteria and guidelines are based on medical evidence and developed in consultation with contracted providers."
    },
    {
        'filename': "GG.1538_CEO20241220_v20241201.pdf",
        'title': "Referral for Second Opinion",
        'description': "This policy defines the process by which CalOptima Health and its contracted Health Networks shall provide a member with a timely referral for a second opinion by an appropriately qualified health care professional. It outlines the conditions under which a second opinion will be authorized, including questioning a diagnosis, treatment plan, or the necessity of a surgical procedure. The policy also addresses the possibility of authorizing a third opinion if the first two opinions differ."
    },
    {
        'filename': "GG.1539_CEO20240523.pdf",
        'title': "Authorization for Out-of-\nNetwork and Out-of-Area\nServices",
        'description': "This policy outlines the requirements and processes for authorizing out-of-network and out-of-area covered services for members assigned to CalOptima Health Direct or a Health Network. It specifies conditions under which CalOptima Health or its delegated Health Networks must authorize such services, including instances where network adequacy requirements are not met or when specialized care is unavailable within the network."
    },
    {
    'filename': "GG.1541_CEO20250129_v20241231.pdf",
    'title': "Utilization Management Delegation",
    'description': "This policy establishes the process by which CalOptima Health assesses and monitors delegated Utilization Management (UM) activities. It outlines the responsibilities of the UM and Delegation Oversight Departments in auditing delegated UM activities. The policy also covers pre-delegation assessments, ongoing monitoring, annual performance reviews, and potential sanctions or de-delegation."
    },
    {
        'filename': "GG.1546_CEO20241220_20241201.pdf",
        'title': "Home Health Services",
        'description': "This policy defines the provision of Home Health Services for Members of CalOptima Health, outlining requirements for prior authorization, medical necessity determination, and member eligibility. It also specifies services excluded from coverage and the requirements for Home Health Agencies providing services to members."
    },
    {
        'filename': "GG.1547_CEO20250129_v20250101.pdf",
        'title': "Maintenance and Transportation",
        'description': "This policy outlines the criteria and process for administering the Maintenance and Transportation benefit for CalOptima Health Members eligible with the California Children’s Services (CCS) program. It details CalOptima Health's responsibilities in authorizing and reimbursing these services for CCS-eligible Members."
    },
    {
        'filename': "GG.1548_v20240201_CEO20240228.pdf",
        'title': "Authorization and Monitoring of Behavioral Health Treatment (BHT) Services",
        'description': "This policy outlines the process for CalOptima Health Members to obtain Medically Necessary Behavioral Health Treatment (BHT) Services. It also describes how CalOptima Health will monitor the provision of these BHT Services, ensuring compliance with regulations and providing necessary early screening, diagnosis, and treatment services."
    },
    {
        'filename': "GG.1549_CEO20241216_v20241201.pdf",
        'title': "Psychological Testing for Mental Health Conditions",
        'description': "This policy outlines the process for CalOptima Health members to receive medically necessary psychological testing for mental health conditions. It specifies criteria for prior authorization, provider qualifications, and the exclusion of certain types of testing like educational or legal system requested tests. The policy also addresses appeals and grievances related to psychological testing services."
    },
    {
        'filename': "GG.1550_CEO20240523.pdf",
        'title': "Palliative Care Services",
        'description': "This policy defines the scope of the Palliative Care program for CalOptima Health Medi-Cal and OneCare Members. It outlines the provision of palliative care services, contracting with qualified providers, and eligibility requirements. Members can access both palliative and curative care if they meet the eligibility criteria."
    },
    {
        'filename': "GG.1600_CEO20241220_v20241201.pdf",
        'title': "Access and Availability Standards",
        'description': "This policy outlines the required access and availability standards for CalOptima Health members to ensure they receive effective and timely care. It covers aspects like provider network adequacy, non-discrimination, accommodations for disabilities, and procedures for religious/ethical objections to providing covered services. The policy also describes the process for CalOptima Health's annual Network Certification."
    },
    {
        'filename': "GG.1602_CEO20241113_v20241001.pdf",
        'title': "Non-Physician Medical Practitioner (NMP) Scope of Practice",
        'description': "This policy establishes a process for ensuring that Non-Physician Medical Practitioners (NMPs) within CalOptima Health's Health Networks have the necessary credentials and supervision to perform their functions. It outlines the scope of practice for NMPs, including requirements for physician supervision, and references credentialing and recredentialing processes. The policy also details specific supervision rules for different types of NMPs, such as Nurse Practitioners, Licensed Midwives, and Certified Nurse Midwives."
    },
    {
        'filename': "GG.1603_CEO20241031_v20241001.pdf",
        'title': "Medical Records Maintenance",
        'description': "This policy defines the minimum standards for maintaining a Member’s Medical Records. It outlines requirements for practitioners, including documentation, access, and storage of records, ensuring compliance with HIPAA and other regulations. CalOptima Health will monitor practitioner compliance through site reviews."
    },
    {
        'filename': "GG.1605_v20231101_CEO20231207.pdf",
        'title': "Delegation and Oversight of\nCredentialing and\nRecredentialing Activities",
        'description': "This policy outlines the processes by which CalOptima Health ensures Credentialing and Recredentialing activities are performed by Delegated Entities in accordance with quality, state, and federal standards. It details the conditions under which CalOptima Health may delegate authority for Medi-Cal screening and enrollment, credentialing, and recredentialing activities to Health Networks or other Delegated Entities. CalOptima Health remains accountable for these activities even if delegated."
    },
    {
        'filename': "GG.1607_CEO20241113_v20241001.pdf",
        'title': "Monitoring Adverse Actions",
        'description': "This policy establishes a process for the ongoing monitoring of actions taken by external entities against CalOptima Health Practitioners or Organizational Providers. It outlines what constitutes an adverse action and specifies monitoring activities to be performed by CalOptima Health and its Health Networks between recredentialing cycles. The policy ensures quality and compliance by identifying and addressing potential risks associated with practitioners and providers."
    },
    {
        'filename': "GG.1608_CEO20241017_v20241001.pdf",
        'title': "Full Scope Site Reviews",
        'description': "This policy outlines CalOptima Health’s site review process, including Facility Site Reviews (FSR), Medical Record Reviews (MRR), and Physical Accessibility Review Surveys (PARS). It describes how CalOptima Health conducts, scores, tracks, and reports site reviews according to state and federal guidelines, ensuring quality, safety, and accessibility of care delivery sites."
    },
    {
        'filename': "GG.1611_CEO20241010_v20241001.pdf",
        'title': "Potential Quality Issue Review Process",
        'description': "This policy outlines the procedure for reviewing and processing Potential Quality Issues (PQIs) referred to the CalOptima Health Quality Improvement (QI) Department. It details how PQIs are identified, investigated, and reported, including roles and responsibilities of various departments and committees. The policy also emphasizes the importance of confidentiality and data trending to identify emerging patterns."
    },
    {
        'filename': "GG.1613_CEO20241122_v20241101.pdf",
        'title': "Initial Health Appointment",
        'description': "This policy outlines CalOptima Health's process for ensuring all members receive an Initial Health Appointment (IHA) within 120 days of enrollment, adhering to relevant statutory, regulatory, and contractual requirements. The IHA must be culturally and linguistically appropriate and include preventive screenings and immunizations based on USPSTF and ACIP guidelines. Primary care visits are leveraged as a proxy for IHA completion, utilizing Managed Care Accountability Sets (MCAS) measures."
    },
    {
        'filename': "GG.1615_CEO20241220_v20241201.pdf",
        'title': "Corrective Action Plan for\nPractitioners and\nOrganizational Providers",
        'description': "This policy defines the Corrective Action process that CalOptima Health uses for Practitioners and Organizational Providers (OPs), including monitoring, investigation, and corrective action related to their clinical practice. It outlines the responsibilities of the Quality Improvement Health Equity Committee (QIHEC), the CEO, and the CMO in overseeing quality improvement activities and ensuring the safety of CalOptima Health Members."
    },
    {
        'filename': "GG.1616__CEO20241220_v20241201.pdf",
        'title': "Fair Hearing Plan for Practitioners",
        'description': "This policy outlines the process CalOptima Health will use to provide practitioners with a fair hearing when adverse actions are proposed or taken that require reporting under California Business and Professions Code Section 805 and/or the National Practitioner Data Bank. It details the procedural rights offered to practitioners and the circumstances under which a hearing can be requested, specifically related to actions taken by or initiated by the practitioner that trigger mandatory reporting."
    },
    {
        'filename': "GG.1617_CEO20241031_v20241001.pdf",
        'title': "Infection Control Plan",
        'description': "This policy provides guidelines for managing contamination and cross-contamination within the ambulatory setting, aiming to prevent the transmission of potentially infectious agents to Members and caregivers. It outlines responsibilities for healthcare workers and CalOptima Health, including training, reporting exposures, and following established infection control precautions."
    },
    {
        'filename': "GG.1618_CEO20250206_v20250201.pdf",
        'title': "Member Request for Medical Records",
        'description': "This policy outlines the responsibilities of Practitioners and Providers in granting Members access to their Medical Records. It details the procedures for accessing, inspecting, and copying protected health information, and it ensures that Members are not denied access due to unpaid bills."
    },
    {
        'filename': "GG.1619_v20231101_CEO20231207_no attachments.pdf",
        'title': "Delegation Oversight",
        'description': "This policy defines the oversight process for Delegated Entities, such as Health Networks and Pharmacy Benefit Managers, to ensure compliance with regulations, contracts, and CalOptima Health policies. It outlines how CalOptima Health monitors performance, conducts audits, and assesses the ability of Delegated Entities to perform delegated functions to ensure continuous improvement of member care."
    },
    {
        'filename': "GG.1620_CEO20240605_v20240601.pdf",
        'title': "Quality Improvement Health Equity Committee (QIHEC)",
        'description': "This policy outlines the purpose and function of CalOptima Health's Quality Improvement Health Equity Committee (QIHEC). The QIHEC is responsible for directing quality management and improvement processes, ensuring quality and equitable health care services, and overseeing the Quality Improvement Health Equity Transformation Plan (QIHETP)."
    },
    {
        'filename': "GG.1621_CEO20241113_v20241001.pdf",
        'title': "Community-Based Adult\nServices (CBAS) Quality\nAssurance and Site Visits",
        'description': "This policy outlines CalOptima Health's process for conducting site visits and monitoring quality assurance at Community-Based Adult Services (CBAS) centers. It ensures that these centers provide services according to member care plans and that audit results are reported to the Quality Improvement Health Equity Committee. The policy also details how CalOptima Health will share findings with the California Department of Aging and monitor deficiencies."
    },
    {
        'filename': "GG.1628__CEO20241220_v20241201.pdf",
        'title': "Confidentiality of Quality Improvement Activities",
        'description': "This policy outlines CalOptima Health's process for maintaining the confidentiality of information related to Members, Practitioners, Providers, and Health Networks, as well as data obtained during Quality Improvement activities, in accordance with applicable laws and standards. It emphasizes the confidential and privileged nature of information associated with the Quality Improvement Health Equity Committee (QIHEC) and its subcommittees."
    },
    {
        'filename': "GG.1629_CEO20240822_v20240601.pdf",
        'title': "Quality Improvement and\nHealth Equity Transformation\nProgram (QIHETP)",
        'description': "This policy outlines CalOptima Health's commitment to quality and equitable healthcare, detailing the development, implementation, and evaluation of the Quality Improvement and Health Equity Transformation Program (QIHETP). The QIHETP focuses on systematically improving health equity and healthcare delivery to members, adhering to relevant laws, regulations, and contracts, with alignment to the Department of Health Care Services (DHCS)."
    },
    {
        'filename': "GG.1630_CEO20241010_v20241001.pdf",
        'title': "Reporting Communicable Diseases",
        'description': "This policy defines the procedures for CalOptima Health and its Health Networks to report serious diseases or conditions to local and state public health authorities, as required by law. It ensures contracted healthcare providers and laboratories report known or suspected cases of diseases to the appropriate jurisdiction, adhering to California state law."
    },
    {
        'filename': "GG.1633_CEO20241122_v20241101.pdf",
        'title': "Board Certification Requirements for Physicians",
        'description': "This policy outlines CalOptima Health's requirements for board certification of its contracted physicians. It specifies the timeframe for achieving board certification after residency and details grandfathering exemptions. It also describes the procedure for verifying board certification status during the credentialing and recredentialing processes."
    },
    {
        'filename': "GG.1634_CEO20240822_v20240601.pdf",
        'title': "Quality Improvement and\nHealth Equity Activities",
        'description': "This policy outlines the guidelines for identifying, developing, and approving Quality Improvement and Health Equity Activities within CalOptima Health. It aims to achieve demonstrable and sustained improvement in clinical and non-clinical areas to improve quality of care, patient safety, health outcomes, and member satisfaction."
    },
    {
        'filename': "GG.1637_CEO20240620_v20240601.pdf",
        'title': "Assessing Member Experience",
        'description': "This policy outlines how CalOptima Health assesses and develops strategies to improve the member experience related to their healthcare and services. It includes data collection on member health status and experiences, participation in CAHPS surveys administered by regulatory agencies, and analysis of complaints, appeals, and survey results."
    },
    {
        'filename': "GG.1639_CEO20241220_20241201.pdf",
        'title': "Post-Hospital Discharge Medication Supply",
        'description': "This policy outlines CalOptima Health's oversight of contracted hospitals to ensure members have access to a 72-hour supply of covered outpatient drugs in emergency situations post-hospital discharge. It details the responsibilities of hospitals, the Quality Improvement Department, Medi-Cal Rx, Customer Service, and Provider Relations in ensuring access to these medications when prior authorization is unavailable."
    },
    {
        'filename': "GG.1643_CEO20241220_20241201.pdf",
        'title': "Minimum Provider Credentialing Standards",
        'description': "This policy outlines the minimum credentialing standards required for providers to participate in CalOptima Health programs. It specifies criteria related to licensing, insurance, program eligibility, and criminal history. The policy applies to Medi-Cal, OneCare, and PACE programs."
    },
    {
        'filename': "GG.1645_CEO20241220_20241201.pdf",
        'title': "Assessing Primary Care Provider (PCP) Experience",
        'description': "This policy outlines the process for collecting and analyzing feedback from Primary Care Providers (PCPs) regarding their experience with CalOptima Health's care delivery system. The aim is to identify areas for improvement and implement quality improvement initiatives based on PCP feedback related to areas like Utilization Management. The Quality Analytics (QA) Department is responsible for coordinating data analysis and distributing results."
    },
    {
        'filename': "GG.1650_CEO20240620_v20240501.pdf",
        'title': "Credentialing and\nRecredentialing of Practitioners",
        'description': "This policy outlines the process CalOptima Health uses to evaluate and determine if practitioners meet the qualifications for participation in its programs. It also addresses the delegation of Medi-Cal screening, enrollment, credentialing, and recredentialing activities to Health Networks or other Delegates, ensuring compliance with applicable laws and regulations."
    },
    {
        'filename': "GG.1651_CEO20241017_v20241001.pdf",
        'title': "Assessment and Reassessment of\nOrganizational Providers",
        'description': "This policy outlines the process CalOptima Health uses to evaluate and determine the eligibility of Organizational Providers (OPs) to participate in its programs. It covers guidelines for evaluation, delegation of Medi-Cal screening and enrollment activities, and assessment/reassessment procedures. The policy also specifies responsibilities of the Chief Medical Officer and the Credentialing and Peer Review Committee."
    },
    {
        'filename': "GG.1652_CEO20241220_v20241201.pdf",
        'title': "DHCS Notification of Change in the\nAvailability or Location of Covered\nServices",
        'description': "This policy outlines the process CalOptima Health follows to notify the Department of Health Care Services (DHCS) about significant changes in the availability of Network Providers or the location of Covered Services. It ensures members are informed of these changes and that DHCS receives prior notification, especially in cases of provider termination or changes impacting service accessibility."
    },
    {
        'filename': "GG.1655_CEO20240924_v20240901.pdf",
        'title': "Reporting Provider Preventable Conditions (PPC)",
        'description': "This policy outlines CalOptima Health's procedure for reporting Provider Preventable Conditions (PPC) to the Department of Health Care Services (DHCS). It details which PPC events must be reported, and how CalOptima Health screens claims and encounter data to identify these conditions."
    },
    {
        'filename': "GG.1656_CEO20241010_v20241001.pdf",
        'title': "Quality Improvement and\nUtilization Management\nConflicts of Interest",
        'description': "This policy outlines CalOptima Health's requirements for identifying, disclosing, and evaluating conflicts of interest within the Quality Improvement (QI) and Utilization Management (UM) departments. It aims to ensure that decisions regarding member care and treatment are made solely in the best interests of the members, free from any actual or perceived conflicts. The policy also extends to delegated health networks, requiring them to have consistent procedures for managing conflicts of interest."
    },
    {
        'filename': "GG.1657_CEO20241031_v20241001.pdf",
        'title': "State Licensing Board and\nthe National Practitioner\nData Bank (NPDB)\nReporting",
        'description': "This policy outlines CalOptima Health's and its delegated Health Networks' responsibilities for complying with State Licensing Board and National Practitioner Data Bank (NPDB) requirements. It details the reporting of certain actions related to CalOptima Health Practitioner and Organizational Provider credentialing and peer review activities, including denials, non-renewals, restrictions, and terminations."
    },
    {
        'filename': "GG.1658_CEO20241220_20241201.pdf",
        'title': "Summary Suspension or Restriction of Practitioner Participation in CalOptima Health’s Network",
        'description': "This policy outlines the process CalOptima Health will use to implement a summary suspension or restriction on a Practitioner due to a Medical Disciplinary Cause or Reason. It details the conditions under which such actions can be taken, notification procedures, and reporting requirements to relevant agencies and data banks. It also ensures that health networks have consistent policies and procedures."
    },
    {
        'filename': "GG.1659_CEO20241216_v20241201.pdf",
        'title': "System Controls and\nConfidentiality of Provider\nCredentialing Information",
        'description': "This policy outlines how CalOptima Health manages and secures provider credentialing information within its credentialing system. It also defines the scope of confidentiality for credentialing files, ensuring that access is restricted and data is protected in accordance with legal and regulatory requirements."
    },
    {
        'filename': "GG.1660_CEO20241220_v20241201.pdf",
        'title': "Federally Qualified Health\nCenter (FQHC) and Rural\nHealth Clinic (RHC) Financial\nIncentives and Pay for\nPerformance Payments",
        'description': "This policy outlines the guidelines CalOptima Health must follow when structuring and implementing financial incentives and Pay for Performance (P4P) payments to Federally Qualified Health Centers (FQHCs) and Rural Health Clinics (RHCs) contracted with CalOptima Health.  It ensures that these payments are designed to avoid inclusion in wrap-around or supplemental payment calculations. The policy also specifies that financial incentives or P4P payments should not be used to pay an FQHC or RHC an additional rate per service based exclusively on utilization."
    },
    {
        'filename': "GG.1661_CEO20240822_v20240701_rev title.pdf",
        'title': "External Quality Review (EQR) Requirements",
        'description': "This policy outlines the guidelines for CalOptima Health's External Quality Review (EQR) requirements as designated by the Department of Health Care Services (DHCS). It details the EQR activities CalOptima Health must participate in, including quality and health equity performance measures, performance improvement projects, and consumer satisfaction surveys."
    },
    {
        'filename': "GG.1665_CEO20241010_v20241001.pdf",
        'title': "Telehealth and Other Technology-Enabled Services",
        'description': "This policy outlines the requirements for coverage and reimbursement of telehealth services provided to CalOptima Health Medi-Cal members. It details the qualifications for providers, the necessary compliance measures, and the conditions under which telehealth can be used to increase network capacity and meet access standards. The policy also emphasizes member rights and the limitations on requiring provider presence at the originating site."
    },
    {
        'filename': "GG.1666_CEO20240711_v20240701.pdf",
        'title': "CalOptima Health Mobile Texting Program",
        'description': "This policy outlines the CalOptima Health Mobile Texting Program, which aims to improve communication with Medi-Cal members through mobile health interactive text messaging services. The program focuses on member engagement, promoting healthy behaviors, and supporting preventive care by delivering notifications, health information, and digital health rewards."
    },
    {
        'filename': "GG.1667_CEO20240822_v20240701.pdf",
        'title': "CalAIM Population Health Management Program",
        'description': "This policy defines CalOptima Health's Population Health Management (PHM) Program and describes the process by which CalOptima Health, Health Networks, and Providers engage Members across delivery systems and carved-out services. The PHM program aims to ensure access to comprehensive services based on individual needs, improve outcomes, and promote Health Equity."
    },
    {
        'filename': "GG.1668_CEO20241220_20241205.pdf",
        'title': "Inpatient Interfacility Transfers",
        'description': "This policy outlines the requirements for coverage of interfacility transfers of admitted inpatients from one acute care facility to another. It specifies the medical necessity criteria that must be met for CalOptima Health to provide coverage and outlines situations where transfers are not considered medically necessary. A prior authorization is required for transfer back to the originating facility when specific criteria are met."
    },
    {
        'filename': "GG.1701_CEO20241025_v20240801.pdf",
        'title': "CalOptima Health Perinatal Support Services (PSS) Program",
        'description': "This policy outlines the guidelines for providing Perinatal Support Services (PSS) to CalOptima Health members, including referrals to contracted providers for obstetric services. It details the provision of enhanced perinatal support services through the Comprehensive Perinatal Services Program (CPSP) and the twelve-month postpartum coverage period for Medi-Cal eligible individuals."
    },
    {
        'filename': "GG.1704_CEO20241113_v20241001.pdf",
        'title': "Breastfeeding Promotion",
        'description': "This policy outlines CalOptima Health's commitment to providing pregnant members with breastfeeding information and services, aligning with recommendations from various health organizations. It details the responsibilities of CalOptima Health, Health Networks, and providers in promoting breastfeeding, including offering educational materials, referrals to support programs, and access to resources like WIC and breast pumps."
    },
    {
        'filename': "GG.1706_v20231201_CEO20231226_no attachments.pdf",
        'title': "Child Abuse Report",
        'description': "This policy outlines the process for assessing and reporting suspected child abuse cases for CalOptima members. It details the responsibilities of mandated reporters, including practitioners, health networks, and contracted providers, to report suspected abuse or neglect to the appropriate authorities within a specified timeframe, following California Penal Code guidelines."
    },
    {
        'filename': "GG.1707_v20240201_CEO20240222_no attachments.pdf",
        'title': "Doula Services",
        'description': "This policy outlines the eligibility requirements for CalOptima Health Doula services, the qualifications for Doula providers, and the provision of CalOptima Health Doula services as a benefit. It details requirements for CalOptima Health and Health Networks related to Doula services for prenatal, perinatal, and postpartum Members."
    },
    {
        'filename': "GG.1713_CEO20240924_v20240901.pdf",
        'title': "Certified Nurse-Midwife Practice Guidelines",
        'description': "This policy defines the practice guidelines for Certified Nurse-Midwives (CNMs) providing covered services to CalOptima Health members. It outlines requirements for access to CNMs, establishment of practice guidelines, credentialing, and scope of practice in accordance with state and federal laws."
    },
    {
        'filename': "GG.1717_CEO20240626_v20240601.pdf",
        'title': "Blood Lead Screening of Young Children",
        'description': "This policy outlines the process by which CalOptima Health ensures the provision of blood lead screenings to members aged six months to seventy-two months. It details compliance with statutory, regulatory, and contractual requirements, including reporting to the Childhood Lead Poisoning Prevention Branch (CLPPB). CalOptima Health is responsible for identifying members under 72 months who have not received blood lead screenings."
    },
    {
        'filename': "GG.1800_CEO20240905_v20240901.pdf",
        'title': "Authorization Process and\nCriteria for Admission to,\nContinued Stay in, and\nDischarge from a Nursing\nFacility Level A (NF-A) and\nLevel B (NF-B)",
        'description': "This policy outlines the requirements for reviewing and processing Long-Term Care (LTC) authorizations for a Member’s admission to, continued stay in, or discharge from a nursing facility under Nursing Facility Level A (NF-A) and Nursing Facility Level B (NF-B) levels of care. It describes CalOptima Health's process for ensuring members receive appropriate nursing facility services based on their medical needs, and it details the documentation and timelines required for facilities submitting authorization requests. The policy also addresses payment reductions for late submissions."
    },
    {
        'filename': "GG.1802_CEO20250109_v20241101.pdf",
        'title': "Authorization Process and\nCriteria for Admission to,\nContinued Stay in, and\nDischarge from an ICF/DD,\nICF/DD-H, and ICF/DD-N",
        'description': "This policy outlines the criteria for a Member’s admission to, continued stay in, or discharge from an Intermediate Care Facility/Developmentally Disabled (ICF/DD), ICF/DD-Habilitative (ICF/DD-H), or ICF/DD-Nursing (ICF/DD-N). It also details the requirements for reviewing and processing ICF/DD, ICF/DD-H and ICF/DD-N Notification Forms, including Regional Center and attending physician certification."
    },
    {
        'filename': "GG.1803_CEO20240905_v20240901.pdf",
        'title': "Authorization Process and\nCriteria for Admission to,\nContinued Stay in, and\nDischarge from a Subacute\nFacility-Adult/Pediatric",
        'description': "This policy outlines the requirements for reviewing and processing Long-Term Care (LTC) Authorizations. It also specifies the criteria for a Member's admission to, continued stay in, or discharge from a Subacute Facility-Adult, or Subacute Facility-Pediatric. The policy applies to Medi-Cal and OneCare programs."
    },
    {
        'filename': "GG.1804_CEO20240905_v20240901.pdf",
        'title': "Admission to, Continued Stay\nin, and Discharge from Out-of-\nNetwork Subacute Facility,\nNursing Facility Level A (NF-A)\nand Level B (NF-B)",
        'description': "This policy outlines the criteria CalOptima Health uses to authorize a member's admission to, continued stay in, or discharge from a qualified, out-of-network subacute or long-term care nursing facility. It addresses situations such as court-ordered placements, short-term rehabilitation, and instances where network nursing facility beds are unavailable, or when a member resides in an out-of-network facility prior to enrollment."
    },
    {
        'filename': "GG.1805_CEO20240924_v20240901.pdf",
        'title': "Distinct Part Nursing Facility",
        'description': "This policy clarifies the circumstances under which CalOptima Health will authorize Distinct-Part Nursing Facility (DP/NF) care based on the Hudman vs. Kizer court order. It outlines the conditions under which DP/NF services shall be reimbursed, focusing on proximity to the member's residence or family and the availability of Free-Standing Nursing Facilities."
    },
    {
        'filename': "GG.1806_CEO20240924_v20240901.pdf",
        'title': "Preadmission Screening and\nResident Review (PASRR)",
        'description': "This policy outlines the Preadmission Screening and Resident Review (PASRR) process for CalOptima Health Members in Long Term Care (LTC) facilities. It details the responsibilities of General Acute Care Hospitals and Skilled Nursing Facilities (SNFs) in completing and reviewing PASRR screenings. The policy also addresses procedures for individuals admitted from community-level settings and the involvement of Level II contractors."
    },
    {
        'filename': "GG.1808_CEO20240924_v20240901.pdf",
        'title': "Plan of Care, Long-Term Care",
        'description': "This policy outlines the requirements for an individually written Plan of Care for CalOptima Health Members admitted to a Long-Term Care (LTC) facility. It aims to ensure coordinated care across medical, behavioral health, and long-term services and supports for these members."
    },
    {
        'filename': "GG.1809_CEO20240924_v20240901.pdf",
        'title': "Retroactive Authorization Request for Long Term Care Facility",
        'description': "This policy outlines the requirements for submitting a retroactive Authorization Request for Long Term Care (LTC) admission to or continued stay in a Skilled Nursing Facility (SNF) for various levels of care. It specifies the conditions under which CalOptima Health's LTSS Department may grant retroactive approval for LTC ARFs and the procedures facilities must follow."
    },
    {
        'filename': "GG.1810_CEO20240924_v20240901.pdf",
        'title': "Bed Hold, Long-Term Care",
        'description': "This policy outlines the process for Long-Term Care (LTC) Bed Holds when a member is transferred to a General Acute Care Hospital. It specifies the conditions under which an LTC facility must hold a bed vacant, the limitations on bed hold days, and the payment structure for bed hold days."
    },
    {
        'filename': "GG.1811_CEO20250109_v20241101.pdf",
        'title': "Leave of Absence, Long-Term Care",
        'description': "This policy outlines the conditions under which CalOptima Health may approve a member's Leave of Absence (LOA) from a Long-Term Care facility. It specifies requirements for facilities, acceptable reasons for LOA, and limitations on the number of approved LOA days per year based on the member's level of care."
    },
    {
        'filename': "GG.1814_CEO20240711_v20240701.pdf",
        'title': "Appeals Process for Long Term Care Facility",
        'description': "This policy outlines the appeals process for Long Term Care (LTC) Facilities to appeal CalOptima Health's post-service Level of Care decisions related to denials, modifications, or alternative recommendations for daily rate services for Medi-Cal, OneCare, or OneCare Connect members. It details the steps and timelines for submitting an appeal after receiving a Notice of Adverse Benefit Determination (NABD) or Notice of Denial."
    },
    {
        'filename': "GG.1815_CEO20241031_v20241001.pdf",
        'title': "Long Term Services and\nSupport Quality of Care\nReporting",
        'description': "This policy outlines the reporting mechanism for concerns regarding events that potentially affect the safety and well-being of Members participating in the Long Term Services and Supports (LTSS) Program. It details the procedures for submitting and reviewing Critical Incident Reports and Complaints related to quality of care."
    },
    {
        'filename': "GG.1816_CEO20250109_v20241101.pdf",
        'title': "Quality Improvement Activities, Long-Term Services and Supports",
        'description': "This policy defines the scope of quality improvement activities related to members participating in the Long-Term Services and Supports (LTSS) Program. It outlines CalOptima Health's compliance with state and federal requirements for LTSS and the responsibilities of the Quality Improvement Program. The policy also describes collaboration between LTSS and QI Departments on quality activities."
    },
    {
        'filename': "GG.1822_CEO20241031_v20241001.pdf",
        'title': "Process for Transitioning CalOptima Health Members between Levels of Care",
        'description': "This policy outlines the process for transitioning CalOptima Health Members between Levels of Care (LOC), as well as into and out of Long-Term Care (LTC). It details responsibilities for acute care facilities, LTC facilities, and CalOptima Health/Health Networks during these transitions, covering aspects like discharge planning, transportation, and bed hold requests."
    },
    {
        'filename': "GG.1826_CEO20241031_v20241001.pdf",
        'title': "MSSP Emergency Preparedness",
        'description': "This policy establishes operational guidelines to ensure the provision of services to meet the emergency needs of Multipurpose Senior Services Program (MSSP) Members during a disaster, emergency, or broad health care surge event. CalOptima Health shall provide information and assistance to Members and their care givers to assist them in preparing for a disaster or emergency event and maintain continuity of care services during such events."
    },
    {
        'filename': "GG.1828_CEO20241031_v20241001.pdf",
        'title': "Community Based Adult Services (CBAS) Reauthorization Process",
        'description': "This policy outlines the reauthorization process for Community Based Adult Services (CBAS) to ensure eligible CalOptima Health members continue to receive CBAS benefits. It details responsibilities, utilization of the CBAS Eligibility Determination Tool, and requirements for reassessment and Individualized Plans of Care."
    },
    {
        'filename': "GG.1829_CEO20241113_v20241001.pdf",
        'title': "Community Based Adult Services (CBAS) Discharge Notification Process",
        'description': "This policy defines the Community-Based Adult Services (CBAS) discharge notification process and requirements. It outlines how CBAS centers should notify CalOptima Health of a Member’s discharge and how CalOptima Health reports discharge reasons to the Department of Health Care Services (DHCS)."
    },
    {
        'filename': "GG.1830_CEO20241113_v20241001.pdf",
        'title': "In-Home Supportive Services (IHSS) Referral Coordination Process",
        'description': "This policy outlines CalOptima Health's process for identifying and referring members who may be eligible for In-Home Supportive Services (IHSS). It details the collaboration and coordination between CalOptima Health and the Orange County Social Services Agency (SSA) regarding IHSS referrals and information sharing. The policy also specifies the responsibilities of both CalOptima Health and SSA in ensuring at-risk members receive the necessary home-based caregiving support."
    },
    {
        'filename': "GG.1831_CEO20241031_v20241001.pdf",
        'title': "Multipurpose Senior Services Program (MSSP)",
        'description': "This policy defines how CalOptima Health ensures access to and provision of Multipurpose Senior Services Program (MSSP) services. The MSSP program provides social and health care management for frail elderly Members who are certified for placement in a nursing facility but desire to remain in the community.  It enables eligible members to remain in or safely return to their homes, providing services at a cost lower than nursing home placement."
    },
    {
        'filename': "GG.1832_CEO20241031_v20241001.pdf",
        'title': "Multipurpose Senior Services Program (MSSP) – MSSP Identification, Referral, and Coordination of Care Process",
        'description': "This policy outlines the process for identifying and referring CalOptima Health Members who may be eligible for the Multipurpose Senior Services Program (MSSP). It aims to ensure at-risk members receive Home and Community-Based Services (HCBS) to maintain quality of care and delay institutionalization. The policy also details coordination between CalOptima Health and MSSP providers."
    },
    {
        'filename': "GG.1834_CEO20241031_v20241001.pdf",
        'title': "Multipurpose Senior Services\nProgram (MSSP) Appeals,\nGrievances and Complaints\nProcess",
        'description': "This policy outlines the process by which the CalOptima Health Multipurpose Senior Services Program (MSSP) Provider tracks and reports Member Appeals, Grievances and Complaints to Long Term Services and Supports (LTSS) and Grievance and Appeal Resolution Services (GARS) Departments. It details the responsibilities of CalOptima Health MSSP Providers and GARS in managing these processes, as well as the member's rights to file appeals, grievances, or complaints."
    },
    {
        'filename': "GG.1900_CEO20250206_v20241231.pdf",
        'title': "Behavioral Health Services",
        'description': "This policy outlines access to Behavioral Health Services for Medi-Cal Members. It details the Non-Specialty Mental Health Services (NSMHS) that CalOptima Health shall offer when recommended by a licensed healthcare professional, including individual/group/family therapy, psychological testing, and medication management support."
    },

    # HH Folder
    {
        'filename': "HH.1101_v20231207_CEO20231207_no attachments.pdf",
        'title': "CalOptima Health Provider Complaint",
        'description': "This policy outlines the process by which CalOptima Health and its associated entities address and resolve complaints from contracted providers, including disputes, appeals, and grievances. It emphasizes maintaining a fast, fair, and cost-effective system while adhering to applicable regulations and contractual requirements, and it prohibits discrimination or retaliation against providers who file complaints."
    },
    {
        'filename': "HH.1102_CEO20240905_v20240901.pdf",
        'title': "Member Grievance",
        'description': "This policy outlines the process by which CalOptima Health addresses and resolves grievances submitted by members, or their representatives, ensuring compliance with relevant regulations and contracts. It details the procedures for receiving, handling, and resolving grievances, emphasizing assistance for members and prompt review of all complaints."
    },
    {
        'filename': "HH.1104_CEO20240912_v20240901.pdf",
        'title': "Discrimination Grievances",
        'description': "This policy ensures that CalOptima Health, Health Networks, Providers, and Practitioners do not discriminate against Members in the provision of Covered Services. It outlines compliance with federal and state nondiscrimination requirements and lists characteristics protected by these laws. The policy also details actions that constitute discrimination and are prohibited."
    },
    {
        'filename': "HH.1105_CEO20241119_v20241107.pdf",
        'title': "Fraud, Waste, and Abuse\nDetection",
        'description': "This policy establishes a process to detect suspected Fraud, Waste, or Abuse (FWA) in a CalOptima Health program by various parties, including members, providers, employees, and related entities. CalOptima Health maintains a zero-tolerance policy toward FWA and outlines procedures for detecting and reporting suspected violations, ensuring compliance with relevant regulations and statutes."
    },
    {
        'filename': "HH.1106_v20231201_CEO20231214_no attachments.pdf",
        'title': "Pay and Educate Criteria—Provider Complaints",
        'description': "This policy outlines the criteria and process by which CalOptima Health may resolve provider or practitioner complaints related to payment denials due to noncompliance with authorization policies. It allows for a 'pay and educate' decision under specific circumstances, such as when a provider is unfamiliar with CalOptima Health's authorization requirements and has not previously received such a resolution."
    },
    {
        'filename': "HH.1107_CEO20241120_v20241107.pdf",
        'title': "Fraud, Waste, and Abuse Investigation and Reporting",
        'description': "This policy establishes a process to investigate and report suspected Fraud, Waste, or Abuse (FWA) committed by members, providers, employees, and related entities within CalOptima Health programs. It outlines CalOptima Health's zero-tolerance policy toward FWA and its commitment to complying with applicable regulations and reporting requirements."
    },
    {
        'filename': "HH.1108_CEO20240912_v20240901.pdf",
        'title': "State Hearing Process and Procedures",
        'description': "This policy defines CalOptima Health’s process, role, and responsibilities in ensuring a Member’s right to access the State Hearing process. It outlines the conditions under which a member can request a State Hearing and CalOptima Health's responsibilities in assisting the member during the process."
    },
    {
        'filename': "HH.1109_v20231201_CEO20231226.pdf",
        'title': "Complaints Decision Matrix",
        'description': "This policy outlines the process for identifying and referring Member and Provider Complaints that require administrative approval for resolution by CalOptima Health. It defines the escalation paths based on the nature of the complaint, such as quality of care or medical necessity denials. It also specifies that providers must exhaust certain internal processes before filing a complaint."
    },
    {
        'filename': "HH.2002_CEO20241120_v20241107.pdf",
        'title': "Sanctions",
        'description': "This policy outlines the process by which CalOptima Health will impose sanctions on First Tier, Downstream, or Related Entities (FDRs) for non-compliance with regulations, contracts, CalOptima Health policies, or failure to implement corrective actions. The policy details the basis for sanctions, the types of sanctions that may be imposed, and the procedures for implementation."
    },
    {
        'filename': "HH.2003_CEO20241031_v20241001.pdf",
        'title': "Health Network and Delegated Entity Reporting",
        'description': "This policy outlines the process for submission and evaluation of reports that a Health Network or Delegated Entity is required to submit to CalOptima Health. It details the responsibilities of both the Health Networks/Delegated Entities and various CalOptima Health departments in ensuring timely and accurate report submissions. The policy also covers the consequences of noncompliance and escalation procedures."
    },
    {
        'filename': "HH.2005_CEO20241119_v20241107.pdf",
        'title': "Corrective Action Plan",
        'description': "This policy outlines the requirements for CalOptima Health and its partners (FDRs) to develop and submit Corrective Action Plans (CAPs) or Immediate Corrective Action Plans (ICAPs) when non-compliant performance is identified by CalOptima Health's Office of Compliance. It ensures that internal departments and FDRs address non-compliance issues within specified timeframes. Failure to comply with CAP or ICAP requirements may result in further action or sanctions."
    },
    {
        'filename': "HH.2007_CEO20241119_v20241107.pdf",
        'title': "Compliance Committee",
        'description': "This policy outlines the role and responsibility of CalOptima Health’s Compliance Committee in ensuring and enforcing compliance with ethical standards, regulatory requirements, contractual obligations, the Compliance Program, including the Fraud, Waste, and Abuse (FWA) Plan and Code of Conduct, and CalOptima Health policies and procedures. The Committee oversees compliance efforts, recommends and monitors internal processes, and reviews the Compliance Plan annually."
    },
    {
        'filename': "HH.2014_CEO20241119_v20241107.pdf",
        'title': "Compliance Program",
        'description': "This policy establishes a Compliance Program for CalOptima Health to ensure and enforce compliance with ethical standards, contractual requirements, applicable federal and state statutes and regulations, and CalOptima Health policies. It outlines the responsibilities of the Board of Directors, Compliance Officer, and other stakeholders in maintaining an effective compliance program."
    },
    {
        'filename': "HH.2015_CEO20240509_no attachments.pdf",
        'title': "Health Networks Claims Processing",
        'description': "This policy outlines the requirements for Health Networks regarding claims settlement practices and CalOptima Health's oversight to ensure compliance. It addresses administrative processes, timely compliance, and dispute resolution mechanisms for healthcare service claims. The policy also covers corrective actions for failures in reimbursement and prohibits unjust payment practices."
    },
    {
        'filename': "HH.2018_CEO20241107_v20241107.pdf",
        'title': "Compliance and Ethics Hotline",
        'description': "This policy establishes procedures for CalOptima Health to receive, document, and manage calls to its Compliance and Ethics Hotline. It details the hotline's purpose, accessibility, confidentiality measures, and the process for reviewing and acting upon reported issues. The policy also emphasizes non-retaliation for good faith reports."
    },
    {
        'filename': "HH.2019_CEO20241120_v20241107.pdf",
        'title': "Reporting Suspected or Actual\nFraud, Waste, or Abuse (FWA),\nViolations of Applicable Laws\nand Regulations, and/or\nCalOptima Health Policies",
        'description': "This policy establishes a structure for reporting suspected misconduct or violations within CalOptima Health, ensuring that Governing Body members, Employees, and First Tier, Downstream and Related Entities (FDRs) can report issues in good faith without fear of retaliation. It emphasizes a commitment to preventing, detecting, and resolving conduct that violates organizational policies, laws, regulations, or program requirements."
    },
    {
        'filename': "HH.2020_CEO20241120_v20241107.pdf",
        'title': "Conducting Compliance Investigations",
        'description': "This policy outlines the process for conducting and overseeing compliance investigations into allegations of violations of the CalOptima Health Code of Conduct, applicable laws and regulations, or CalOptima Health’s policies and procedures. It details the responsibilities of employees, the governing body, and related entities in reporting and investigating incidents of non-compliance."
    },
    {
        'filename': "HH.2021_CEO20241120_v20241107.pdf",
        'title': "Exclusion and Preclusion Monitoring",
        'description': "This policy outlines the process for verifying and monitoring the eligibility of employees, governing body members, FDRs, non-contracted providers, and vendors to participate in CalOptima Health federal and/or state health care programs through state and federal exclusion, preclusion, and ineligible person/entity lists. It ensures that CalOptima Health does not employ or contract with individuals or entities that are suspended, debarred, precluded, or excluded from participation in these programs."
    },
    {
        'filename': "HH.2022_CEO20241119_v20241107.pdf",
        'title': "Record Retention and Access",
        'description': "This policy establishes the requirements for CalOptima Health and its First Tier, Downstream, and Related Entities (FDRs) to retain and make available records, contracts, and other documents for audits or investigations of CalOptima Health programs. It outlines the types of documents that must be retained and made available, including data related to Medicare utilization, medical records, and encounter data. The policy also describes access rights of authorized agencies and consequences for fraud."
    },
    {
        'filename': "HH.2023_CEO20241220_v20241201.pdf",
        'title': "Compliance Training",
        'description': "This policy outlines CalOptima Health's requirements for annual Compliance Training and education for Employees, members of the Governing Body, and First Tier, Downstream, and Related Entities (FDRs). The training covers topics such as Anti-Fraud, Waste and Abuse (FWA), Code of Conduct, Compliance Plan, and HIPAA, ensuring compliance with applicable statutes, regulations, and CalOptima Health policies."
    },
    {
        'filename': "HH.2025_v20231101_CEO20231207_no attachments.pdf",
        'title': "Health Network Subdelegation\nand Subcontracting",
        'description': "This policy outlines the requirements and processes for Health Network Subdelegation and Subcontracting. It details the conditions under which a Health Network can delegate administrative functions and the oversight responsibilities that remain with the Health Network. CalOptima Health's written approval is required for Subdelegation."
    },
    {
        'filename': "HH.2027_v20231101_CEO20231207_no attachments.pdf",
        'title': "Annual Risk Assessment (FDR)",
        'description': "This policy outlines the annual risk assessment process conducted by CalOptima Health's Delegation Oversight Department to identify compliance risks within First Tier, Downstream, and Related Entities (FDRs). The risk assessment informs the development of CalOptima Health’s FDR audit and monitoring work plan to ensure regulatory obligations are met. It also requires FDRs to conduct their own risk assessments and monitoring of downstream entities."
    },
    {
        'filename': "HH.2028_CEO20241205_v20241107_2025.pdf",
        'title': "Code of Conduct",
        'description': "This policy outlines CalOptima Health's expectations for ethical and legal conduct among employees, governing body members, and FDRs, requiring compliance with the Code of Conduct. It details the process for reviewing, approving, distributing, and monitoring adherence to the Code of Conduct, including annual attestations and consequences for non-compliance."
    },
    {
        'filename': "HH.3000_CEO20241119_v20241107.pdf",
        'title': "Notice of Privacy Practices",
        'description': "This policy outlines the required content and distribution process for CalOptima Health's Notice of Privacy Practices (NPP) to its members. It describes the controls for accessing member data, including Protected Health Information (PHI) and Personally Identifiable Information (PII), and specifies the permissible and impermissible uses of this data."
    },
    {
        'filename': "HH.3001_CEO20241119_v20241001.pdf",
        'title': "Member Access to Designated\nRecord Set",
        'description': "This policy defines the Designated Record Set (DRS) containing Protected Health Information (PHI) for CalOptima Health members. It outlines the conditions under which members, or their representatives, can access, inspect, or obtain copies of their PHI in the DRS, including access through a Patient Access API. The policy also details procedures for requesting access and reporting violations."
    },
    {
        'filename': "HH.3002_CEO20241119_v20241107.pdf",
        'title': "Minimum Necessary Uses and\nDisclosure of Protected Health\nInformation and Document\nControls",
        'description': "This policy outlines the conditions under which CalOptima Health controls access to, requests, uses, or discloses Protected Health Information (PHI) and Personally Identifiable Information (PII). It aims to ensure that only the Minimum Necessary data is used to fulfill requests or carry out required functions, in accordance with HIPAA regulations."
    },
    {
        'filename': "HH.3003_CEO20241119_v20241001.pdf",
        'title': "Verification of Identity for\nDisclosure of Protected Health\nInformation",
        'description': "This policy outlines the necessary steps to verify the identity of individuals requesting Protected Health Information (PHI) before it is disclosed. It details procedures for verifying the identity of both members and their personal representatives through various methods, including telephone, in-person interactions, and written requests."
    },
    {
        'filename': "HH.3004_CEO20241120_v20241107.pdf",
        'title': "Member Request to Amend Records",
        'description': "This policy outlines the process for members to request amendments to their Protected Health Information (PHI) maintained by CalOptima Health. It details the member's right to request corrections, the organization's right to approve or deny such requests, and the procedures involved in processing these amendment requests."
    },
    {
        'filename': "HH.3005_CEO20241120_v20241107.pdf",
        'title': "Member Request for Accounting of Disclosures",
        'description': "This policy outlines a CalOptima Health member's right to request an accounting of disclosures of their Protected Health Information (PHI) made by CalOptima Health, including disclosures to or by its Business Associates, within a six-year period. It also defines exclusions to what must be accounted for and conditions under which a request may be temporarily suspended."
    },
    {
        'filename': "HH.3006_CEO20241120_v20241107.pdf",
        'title': "Tracking and Reporting Disclosures of Protected Health Information",
        'description': "This policy outlines the process CalOptima Health uses to track and report disclosures of a member's Protected Health Information (PHI). It details which disclosures must be tracked and reported internally, and those that are exempt. The policy also specifies procedures for both routine and non-recurring disclosures."
    },
    {
        'filename': "HH.3007_CEO20241120_v20241107.pdf",
        'title': "Member Rights to Request\nRestrictions on Use and\nDisclosure of Protected Health\nInformation",
        'description': "This policy outlines the process by which a CalOptima Health member can request restrictions on the use and disclosure of their Protected Health Information (PHI). It details the conditions under which CalOptima Health may approve or deny such requests, and the exceptions to those restrictions."
    },
    {
        'filename': "HH.3008_CEO20241119_v20241107.pdf",
        'title': "Member Right to Request\nConfidential Communications",
        'description': "This policy outlines the process by which CalOptima Health members can request to receive confidential communications regarding their Protected Health Information (PHI). It details how CalOptima Health accommodates these requests, particularly when there's a risk of personal danger or for sensitive services, ensuring member privacy and safety."
    },
    {
        'filename': "HH.3009_CEO20241120_v20241107.pdf",
        'title': "Access by Member’s Personal Representative",
        'description': "This policy defines the parameters for recognizing a Member’s Personal Representative as having the right to access the Member’s Protected Health Information (PHI). It outlines how CalOptima Health shall treat a Member’s Personal Representative, adhering to state and federal regulations when identifying Personal Representatives and disclosing PHI to them, including specific scenarios for adults, minors, and decedents."
    },
    {
        'filename': "HH.3010_CEO20241119_v20241107.pdf",
        'title': "Protected Health Information\nDisclosures Permitted and\nRequired by Law",
        'description': "This policy outlines how CalOptima Health uses and discloses Protected Health Information (PHI) as permitted by HIPAA and required by law. It details the specific circumstances under which PHI can be disclosed, including member requests, legal requirements, and investigations, while also addressing restrictions related to reproductive healthcare information."
    },
    {
        'filename': "HH.3011_CEO20241120_v20241107.pdf",
        'title': "Use and Disclosure of PHI for Treatment, Payment, and Health Care Operations",
        'description': "This policy outlines the requirements for using and disclosing Member Protected Health Information (PHI) for Treatment, Payment, and Health Care Operations, ensuring compliance with federal and state laws. CalOptima Health can use and disclose PHI without authorization for these purposes, adhering to HIPAA and other protective laws."
    },
    {
        'filename': "HH.3012_CEO20240725_v20240701.pdf",
        'title': "Non-Retaliation for Reporting Violations",
        'description': "This policy reinforces CalOptima Health's commitment to compliance and prohibits retaliation against individuals who report suspected non-compliance with laws, regulations, policies, or unethical conduct. It outlines protections for those who report in good faith or participate in investigations, and mandates reporting any suspected retaliation."
    },
    {
        'filename': "HH.3014_CEO20241119_v20241107.pdf",
        'title': "Use of Electronic Mail with Protected\nHealth Information (PHI) and\nPersonally Identifiable Information\n(PII)",
        'description': "This policy outlines CalOptima Health’s procedures for using electronic mail (email) to send information containing Protected Health Information (PHI) and Personally Identifiable Information (PII). It details requirements for internal and external emails, including encryption and limiting the use of PHI/PII to the minimum necessary data. The policy also references related policies on acceptable use of technology resources and data controls."
    },
    {
        'filename': "HH.3015_CEO20241119_v20241001.pdf",
        'title': "Member Authorization for the Use and\nDisclosure of Protected Health\nInformation",
        'description': "This policy outlines the process for obtaining a member's authorization for the use and disclosure of their Protected Health Information (PHI). It specifies when authorization is required, the conditions under which CalOptima Health will use or disclose PHI, and the required elements of a valid authorization form. The policy also clarifies exceptions where authorization is not needed, such as for treatment, payment, and healthcare operations as permitted by HIPAA."
    },
    {
        'filename': "HH.3016_CEO20241119_v20241107.pdf",
        'title': "Guidelines for Handling Protected Health Information Off-site",
        'description': "This policy outlines the procedures for CalOptima Health employees to follow when handling Protected Health Information (PHI) outside of the main office. It describes precautions to maintain privacy and security in accordance with HIPAA and CalOptima Health policies when creating, accessing, or transporting PHI."
    },
    {
        'filename': "HH.3019_CEO20241120_v20241107.pdf",
        'title': "De-identification of Protected Health\nInformation",
        'description': "This policy outlines CalOptima Health's processes for de-identifying Protected Health Information (PHI) in accordance with HIPAA. It details the permitted uses and disclosures of PHI for creating non-identifiable health information, emphasizing the use of either the Expert Reviewer Method or the Removal of Specific Identifier process (Safe Harbor Method) to de-identify member data."
    },
    {
        'filename': "HH.3020_CEO20241119_v20241107.pdf",
        'title': "Reporting and Providing Notice\nof Security Incidents, Breaches\nof Unsecured PHI/PII or other\nUnauthorized Use or Disclosure\nof PHI/PII",
        'description': "This policy outlines CalOptima Health's procedures for reporting security incidents, breaches of unsecured Protected Health Information/Personally Identifiable Information (PHI/PII), or unauthorized access/disclosure of PHI/PII to regulators. It also details the process for notifying affected members and the media of breaches of unsecured PHI, in accordance with contractual and regulatory requirements. The policy mandates reporting within 24 hours of discovery and includes investigation and mitigation procedures."
    },
    {
        'filename': "HH.3022_CEO20241113_v20241107.pdf",
        'title': "Business Associate Agreements",
        'description': "This policy outlines the guidelines for CalOptima Health's Business Associate Agreements (BAA) with individuals or entities considered Business Associates. It ensures that all service agreements involving Business Associates include a BAA that meets HIPAA and DHCS contract requirements. CalOptima Health will not disclose PHI without an executed BAA and must use its standard BAA template unless otherwise approved."
    },
    {
        'filename': "HH.3023_CEO20241113_v20241001.pdf",
        'title': "Information Sharing",
        'description': "This policy establishes CalOptima Health’s process to share information with participating entities, local health jurisdictions, and other agencies for coordinating Medicare and Medi-Cal Covered Services. It outlines compliance with data sharing exchanges, privacy laws, and the California Health and Human Services Data Exchange Framework."
    },
    {
        'filename': "HH.3024_CEO20241119_v20241107.pdf",
        'title': "Confidentiality of Medical Information",
        'description': "This policy outlines CalOptima Health's commitment to complying with the California Confidentiality of Medical Information Act (CMIA) to protect patient medical information. It details restrictions on sharing, selling, or using medical information without proper authorization and emphasizes the importance of adhering to member communication preferences and privacy rights, particularly regarding sensitive services."
    },
    {
        'filename': "HH.4001_v20231101_CEO20231207_no attachments.pdf",
        'title': "Delegation Oversight Committee",
        'description': "This policy outlines the functions and responsibilities of the Delegation Oversight Committee (DOC) regarding the oversight of CalOptima Health’s First Tier, Downstream, and Related Entities (FDRs). It details the committee's activities, including monitoring, auditing, reporting, and recommending sanctions for FDRs to ensure compliance and quality healthcare."
    },
    {
        'filename': "HH.5000_CEO20241119_v20241107.pdf",
        'title': "Provider Overpayment Investigation and Determination",
        'description': "This policy outlines CalOptima Health's system for reviewing suspect claims to detect and prevent Fraud, Waste, and Abuse (FWA), identify resulting Overpayments, and ensure compliance with federal and state regulations. It details the responsibilities of the Special Investigations Unit (SIU) in identifying overpayment opportunities and investigating potential FWA, as well as procedures for identifying and investigating overpayments."
    },
    {
        'filename': "HH.5004_CEO20241120_v20241107.pdf",
        'title': "False Claims Act Education",
        'description': "This policy establishes CalOptima Health’s process to inform employees, governing body members, and FDRs of their obligations for sharing information regarding compliance with the False Claims Act. It addresses federal and state False Claims Act education requirements, including penalties for submitting false claims and whistleblower protections.  The policy outlines what constitutes a false claim for healthcare providers."
    },

    # MA Folder
    {
        'filename': "MA.4015_CEO20241216_v20241201.pdf",
        'title': "Medicare Secondary Payer\n(MSP)/Part D Coordination of\nBenefits (COB)",
        'description': "This policy outlines CalOptima Health’s process to ensure medical claims are paid in the proper sequence if Other Health Coverage (OHC) has been identified and verified for a OneCare Member. It describes the Coordination of Benefits (COB) process when a OneCare Member has OHC in addition to Medicare. The policy also details how CalOptima Health's Enrollment & Reconciliation (E&R) staff should update member data systems and handle situations where a member's EGHP terminates."
    },
    {
        'filename': "MA.9009_v20231207_CEO20231207_no attachments.pdf",
        'title': "Non-Contracted Provider Complaint Process",
        'description': "This policy outlines the process by which CalOptima Health ensures Non-Contracted Providers (NCPs) have a clear and reliable complaint process, meeting CMS requirements. It details how CalOptima Health and Health Networks handle complaints, provide opportunities for evidence presentation, and process Provider Dispute Resolutions (PDRs) and NCP claims payment Appeals within specified timeframes."
    },
    {
        'filename': "MA.3105_v20240404.pdf",
        'title': "Medicare Secondary Payer",
        'description': "This policy outlines CalOptima Health's process for identifying and recovering conditional payments made for OneCare members when other health coverage is primary. It details situations where OneCare acts as a Medicare Secondary Payer and the procedures for reimbursement from primary payers. The policy also addresses subrogation and recovery rights, ensuring CalOptima Health can recover conditional payments."
    },
    {
        'filename': "MA.9005__Policy_CEO20221221_PRC7a20221212_v.20221201_CEO.pdf",
        'title': "Payment Appeal",
        'description': "This policy defines the procedures by which CalOptima Health shall ensure that an Enrollee has clear and reliable access to a Payment Appeal process that meets the requirements of the Centers for Medicare & Medicaid Services (CMS). It outlines the process for handling and disposing of Payment Appeals, including notification to enrollees and processing timeframes. The policy also covers the rights of enrollees and other parties to initiate a Payment Appeal."
    },
    {
        'filename': "MA.6115_CEO20250109_v20241231.pdf",
        'title': "Medicare Part B Organization Determination (OD)",
        'description': "This policy outlines CalOptima Health’s process for determining drug benefit coverage and/or payment of drug benefits for Medicare Part B. It defines what constitutes an Organization Determination (OD), who can request one, and the rights of members in relation to ODs. The policy also covers Medicare Part B exceptions and timeframes for making ODs."
    },
    {
        'filename': "MA.4007_CEO20241216_v20241201.pdf",
        'title': "Member Disclosures",
        'description': "This policy outlines the requirements for disclosing information to members, ensuring they meet Centers for Medicare & Medicaid Services (CMS) standards. It details the information that CalOptima Health must disclose to members at enrollment and annually, including service area, covered services, access requirements, emergency services coverage, and formulary information."
    },
    {
        'filename': "MA.2100_CEO20241010_v20241001.pdf",
        'title': "Telehealth and Other Technology-Enabled Services",
        'description': "This policy outlines the requirements for coverage and reimbursement of telehealth and other technology-enabled services provided to CalOptima Health OneCare members. It specifies conditions regarding geographic location, eligible services, originating sites, qualified providers, and the use of interactive audio and video telecommunications. The policy also addresses other technology-enabled services like virtual check-ins, e-visits, and remote monitoring."
    },
    {
        'filename': "MA.4016_CEO20241031_v20241001.pdf",
        'title': "Direct Member Reimbursement for Covered Services",
        'description': "This policy outlines the circumstances and requirements under which CalOptima Health or a Health Network may directly reimburse a OneCare Member for covered health care expenses rendered by a Provider upon completion of a coverage decision. It details the conditions under which members are eligible for reimbursement and the responsibilities of CalOptima Health and its Health Networks. The policy also specifies the procedures for requesting and processing direct member reimbursements."
    },
    {
        'filename': "MA.2001_CEO20241122_v20241101.pdf",
        'title': "Marketing Material Standards",
        'description': "This policy outlines CalOptima Health’s guidelines for the creation and distribution of OneCare (HMO D-SNP), a Medicare Medi-Cal plan, marketing materials. It details the distinctions between communication and marketing materials, and specifies requirements for content and usage. The policy ensures compliance with federal regulations and guidelines for marketing activities."
    },
    {
        'filename': "MA.5013_CEO20241216_v20241201.pdf",
        'title': "Pharmacy Audits and Reviews",
        'description': "This policy outlines the processes for CalOptima Health to ensure that Participating Pharmacies adhere to program policies, procedures, and regulatory/contractual requirements. It covers delegation of audit authority, performance standards for pharmacies, and the appeal process for audit findings."
    },
    {
        'filename': "MA.6022_CEO20240711_v20240701.pdf",
        'title': "Initial and Annual Health Risk Assessment",
        'description': "This policy outlines the process for CalOptima Health to conduct initial and annual Health Risk Assessments (HRAs) for OneCare Members, ensuring compliance with statutory, regulatory, and contractual requirements. The HRA aims to identify a Member’s health care needs, including Medi-Cal services, long-term support needs, and social determinants of health, to inform the Individualized Care Plan."
    },
    {
        'filename': "MA.1005_CEO20240509.pdf",
        'title': "Hospital Acquired Conditions –\nReimbursement",
        'description': "This policy outlines the reimbursement guidelines for Hospital Acquired Conditions (HACs) under the OneCare program.  Following CMS regulations, OneCare will not reimburse for specified HACs, meaning hospitals won't receive additional payment if these conditions were not present on admission. The policy lists the specific categories of HACs for which reimbursement will be denied."
    },
    {
        'filename': "MA.6030_v20240101_CEO20240129_no attachments.pdf",
        'title': "Transition of Care",
        'description': "This policy defines the process for managing members at risk for planned and unplanned transitions across the care continuum. It outlines CalOptima Health's Transition of Care program, which focuses on identifying members at risk and facilitating their movement between various care settings. The policy also emphasizes the importance of liaisons for Long-Term Services and Supports (LTSS) and evidence-based interventions to prevent readmissions and ensure coordinated care."
    },
    {
        'filename': "MA.3103_20250221.pdf",
        'title': "Claims Coordination of Benefits",
        'description': "This policy establishes a process for payment of services rendered to a Member who is covered under Medi-Cal or any Other Health Coverage (OHC). It outlines how CalOptima Health will identify primary and secondary payers, determine payable amounts, and coordinate benefits for Members with OHC, including when the member is covered under Medi-Cal."
    },
    {
        'filename': "MA.6024_CEO20241220_20241201.pdf",
        'title': "Notification of Inpatient Facility Discharge Appeal Rights",
        'description': "This policy outlines the procedure for inpatient facilities to provide written notification to members regarding their inpatient facility rights and discharge appeal rights. It details the process for delivering the Important Message from Medicare (IM) Notice and the member's right to appeal a discharge. The policy also specifies the information that must be included in the IM Notice."
    },
    {
        'filename': "MA.4003_CEO20241216_v20250101.pdf",
        'title': "Member Enrollment",
        'description': "This policy outlines the procedures for enrolling individuals in the CalOptima Health OneCare program. It details the eligibility requirements that an individual must meet to enroll, including criteria related to residency, age, Medicare and Medi-Cal status, and U.S. citizenship. The policy also specifies various election periods applicable to enrollment."
    },
    {
        'filename': "MA.6113_CEO20241216_v20241201.pdf",
        'title': "Hospice and Part D\nCoordination of Benefits",
        'description': "This policy outlines the coordination of benefits between Hospice and OneCare Part D programs to ensure appropriate payment for prescription drugs while maintaining member access to necessary medications. It details which drugs are covered under the Hospice benefit and how CalOptima Health prevents duplicate payments. The policy also covers coverage determination processes and retrospective recoveries."
    },
    {
        'filename': "MA.9006_v20231207_CEO20231207_no attachments.pdf",
        'title': "Contracted Provider Complaint Process",
        'description': "This policy outlines the process by which CalOptima Health, Health Networks, and Third Party Administrators (TPAs) address and resolve Contracted Provider Complaints, including Provider Dispute Resolution (PDR), Appeals, and Grievances. It ensures a fast, fair, and cost-effective system for handling these complaints in accordance with relevant regulations and contractual requirements, while also prohibiting discrimination or retaliation against providers who file complaints."
    },
    {
        'filename': "MA.6042_CEO20241220_20241201.pdf",
        'title': "Integrated Organization Determinations",
        'description': "This policy outlines the standards and timeframes by which CalOptima Health or a Health Network shall make Integrated Organization Determinations (IOD) for a Member. It details the process for approving or denying coverage of services, including standard and expedited IODs, and notification requirements for members."
    },
    {
        'filename': "MA.9015_20250221.pdf",
        'title': "Standard Integrated Appeals",
        'description': "This policy outlines the standard process for Integrated Appeals involving Medi-Cal and Medicare Covered Services and benefits, ensuring compliance with CMS and DHCS requirements. It details the procedures for handling appeals, including timelines, rights of appealing parties, and processes for different types of appeals."
    },
    {
        'filename': "MA.5007_CEO20241031_v20241001.pdf",
        'title': "Health Network Encounter Data Performance Standards",
        'description': "This policy outlines CalOptima Health's process for measuring a Health Network's compliance with Encounter data performance standards for services rendered to CalOptima Health OneCare Members, starting January 1, 2024. It specifies rejection rate and timeliness requirements for Encounter submissions and describes the consequences for non-compliance, including potential Corrective Action Plans."
    },
    {
        'filename': "MA.3101_CEO20240509.pdf",
        'title': "Claims Processing",
        'description': "This policy outlines the guidelines for timely and accurate claims processing and adjudication by CalOptima Health or a Health Network, ensuring compliance with relevant regulations. It specifies reimbursement procedures for covered services, submission timelines for providers, and payment protocols for non-contracted providers in specific scenarios such as emergency services and out-of-network care."
    },
    {
        'filename': "MA.2022_CEO20240822_v20240801.pdf",
        'title': "Sales and Marketing Ethics",
        'description': "This policy outlines the process by which CalOptima Health ensures that Community Partners conduct sales and marketing activities in accordance with the CalOptima Health Code of Conduct. It describes the monitoring mechanisms used to ensure compliance with state and federal requirements related to these activities."
    },
    {
        'filename': "MA.6026_v20240101_CEO20240129.pdf",
        'title': "Coordination of Care, Medi-Cal Covered Services for OneCare",
        'description': "This policy defines the process by which CalOptima Health and a Health Network shall coordinate Medi-Cal Covered Services for its Members. It outlines responsibilities for CalOptima Health and Health Networks in coordinating requests, notifying providers, processing claims, and ensuring members exhaust Medicare benefits before accessing Medi-Cal Covered Services. The policy also addresses Enhanced Case Management and continuity of care."
    },
    {
        'filename': "MA.4005_CEO20241216_v20241201.pdf",
        'title': "OneCare Election Periods and Effective Dates",
        'description': "This policy outlines the different election periods available to OneCare members for enrollment and disenrollment. It details the Annual Election Period (AEP), Initial Coverage Election Period (ICEP), Initial Enrollment Period for Part D (IEP-D), Special Election Periods (SEP), Medicare Advantage Open Enrollment Period (MA OEP), and Open Enrollment for Institutionalized Individuals (OEPI)."
    },
    {
        'filename': "MA.6106_CEO20241031_v20250101_2025.pdf",
        'title': "Medication Therapy Management",
        'description': "This policy defines CalOptima Health’s Medication Therapy Management (MTM) program in compliance with CMS standards. It outlines the program's elements, including enhancing member understanding of medications, reducing adverse events, increasing medication adherence, and detecting adverse drug events. CalOptima Health also identifies eligible members and provides MTM services."
    },
    {
        'filename': "MA.3001_CEO20240523.pdf",
        'title': "Payment Arrangements to\nHealth Networks – Capitation\nPayments",
        'description': "This policy outlines the process for timely and accurate Capitation Payments to Health Networks, particularly within the OneCare program. It details how CalOptima Health makes these payments, adjusts them for retroactive changes, handles disputes, and manages potential recoupments or rate adjustments based on CMS funding or internal methodologies."
    },
    {
        'filename': "MA.6109_CEO20241216_v20241201.pdf",
        'title': "True Out-of-Pocket (TrOOP) Expenditures",
        'description': "This policy outlines the process for CalOptima Health to track a member's True Out-of-Pocket (TrOOP) expenditures for covered Part D drugs. It details how the Pharmacy Benefit Manager (PBM) tracks expenditures, how information is collected and shared with members, and how data from other sources is used in the calculation."
    },
    {
        'filename': "MA.9124_CEO20241120_v20241107.pdf",
        'title': "CMS Self-Disclosure",
        'description': "This policy establishes a process for self-disclosing instances of significant Medicare program non-compliance to CalOptima Health’s Centers for Medicare & Medicaid Services (CMS) Regional Account Manager and/or the Department of Health Care Services (DHCS) Contract Manager. The policy ensures that corrective actions are taken promptly when non-compliance incidents are identified and reported to the Office of Compliance. It encourages internal and external business units to voluntarily identify, disclose, and correct non-compliance incidents."
    },
    {
        'filename': "MA.9110_CEO20240605_v20240601.pdf",
        'title': "Auditing and Monitoring of\nHierarchical Condition Categories\n(HCC) Coding",
        'description': "This policy establishes a Hierarchical Condition Categories (HCC) auditing and monitoring process. It aims to ensure CalOptima Health Providers' compliance with documentation and coding guidelines defined by CMS and the OIG. The policy outlines requirements for medical record documentation, diagnosis coding, and provider responsibilities."
    },
    {
        'filename': "MA.2101_CEO20240808_v20240801.pdf",
        'title': "Non-Monetary Member Incentive",
        'description': "This policy establishes CalOptima Health’s standards for the appropriate use of Non-Monetary Member Incentives for the CalOptima Health OneCare Program. It outlines the guidelines for using incentives to increase member participation, learning, and motivation for improving health outcomes while adhering to CMS guidelines."
    },
    {
        'filename': "MA.3002_CEO20240808_v20240801.pdf",
        'title': "Financial Security Requirements",
        'description': "This policy outlines the requirements for Health Networks within the OneCare program to establish and maintain financial security reserves, as mandated by their Health Network Service Agreement. It details the required amount, acceptable forms of financial security instruments, and the circumstances under which the reserves can be utilized. CalOptima Health monitors these reserves to ensure their adequacy and protect the interests of members."
    },
    {
        'filename': "MA.5012_CEO20241122_v20241101.pdf",
        'title': "Pharmacy Network: Credentialing and Access",
        'description': "This policy establishes the standards for pharmacy credentialing and access within the CalOptima Health network. It outlines the procedures for the Pharmacy Benefit Manager (PBM) to determine if pharmacies meet credentialing standards and ensures members have adequate geographic access to participating pharmacies."
    },
    {
        'filename': "MA.4010_CEO20241216_v20241201.pdf",
        'title': "Health Network and Primary Care\nProvider Selection, Assignment,\nand Notification",
        'description': "This policy outlines CalOptima Health's procedures for member selection or assignment to a Health Network and Primary Care Provider (PCP). It also describes the process for notifying members of a PCP contract termination. The policy applies to OneCare members."
    },
    {
        'filename': "MA.7020_CEO20241220_v20241201.pdf",
        'title': "Behavioral Health Services",
        'description': "This policy defines the scope of Behavioral Health Services for OneCare Members, outlining the specific services CalOptima Health shall offer, including inpatient and outpatient mental health services, assessment screenings, and adherence to parity requirements for mental health and substance use disorder treatment. It also addresses privacy protocols for Member's Protected Health Information (PHI)."
    },
    {
        'filename': "MA.4001_CEO20241031_v20241001.pdf",
        'title': "Member Rights and\nResponsibilities",
        'description': "This policy outlines a Member’s rights and responsibilities within CalOptima Health's OneCare program and the process by which CalOptima Health communicates these to Members. It details member rights such as access to information, respectful treatment, and the right to file complaints, as well as member responsibilities like understanding covered services and informing providers of their enrollment."
    },
    {
        'filename': "MA.2030_CEO20241122_v20241101.pdf",
        'title': "Personal/Individual Marketing Appointments",
        'description': "This policy outlines the process for CalOptima Health Community Partners to provide prospective members with information about CalOptima Health OneCare, a Medicare Medi-Cal Plan, through personal/individual marketing appointments. It details the requirements for setting up appointments, conducting them, and ensuring the prospective member understands the information presented."
    },
    {
        'filename': "MA.4011_CEO20241216_v20241201.pdf",
        'title': "OneCare Member Notification of\nChange in Location or Availability\nof Providers or Covered Services",
        'description': "This policy outlines the processes CalOptima Health will use to notify OneCare members about changes in the location or availability of providers and/or covered services. It details notification timelines and requirements related to provider terminations and other significant changes, ensuring compliance with CMS regulations."
    },
    {
        'filename': "MA.9007_v20231201_CEO20231214_no attachments_revised.pdf",
        'title': "Appeal Process for Member Discharge from Inpatient Facility",
        'description': "This policy defines the process by which a member may appeal an organization's decision to discharge them from an inpatient facility. It outlines the steps for requesting immediate review by the Quality Improvement Organization (QIO) and the responsibilities of CalOptima Health. The policy also addresses expedited appeals if the immediate review is not requested."
    },
    {
        'filename': "MA.9008_v20231201_CEO20231214_no attachments.pdf",
        'title': "Appeal Process for Coverage\nTermination of SNF, Home\nHealth, or CORF Services",
        'description': "This policy outlines the process for members to appeal an Organization Determination regarding the termination of Skilled Nursing Facility (SNF), Home Health Agency (HHA), or Comprehensive Outpatient Rehabilitation Facility (CORF) covered services. It details how members can request a fast-track review by the Quality Improvement Organization (QIO) or an expedited review from CalOptima Health."
    },
    {
        'filename': "MA.6044_CEO20241220_20241201.pdf",
        'title': "Coverage of Solid Organ and\nStem Cell Transplants",
        'description': "This policy defines the coverage of Solid Organ and Stem Cell Transplants and related care and services for CalOptima Health Members in the OneCare Program. It outlines the conditions under which these transplants are considered covered services, including pre-transplant evaluation, transplant care, and post-transplant care, while also specifying transplants that are not approved."
    },
    {
        'filename': "MA.2017_CEO20241122_v20241101.pdf",
        'title': "Training and Oversight of Field\nMarketing Organization\n/Broker Agency and\nSubcontracted Independent\nAgents",
        'description': "This policy outlines the training and oversight requirements for Field Marketing Organizations (FMOs), Broker Agencies, and their subcontracted Independent Agents who are involved in marketing CalOptima Health's OneCare program. It ensures compliance with federal and state regulations, including CMS guidelines, related to Medicare marketing and communications."
    },
    {
        'filename': "MA.6104_CEO20241031_v20241001.pdf",
        'title': "Opioid Medication Utilization Management",
        'description': "This policy outlines the process by which CalOptima Health identifies and minimizes potential opioid medication overutilization among OneCare and PACE members. It describes the drug Utilization Management programs that assist in preventing prescribed medication overutilization and aims to reduce fraud, waste, and abuse in the Part D Drug program. The policy also ensures compliance with applicable statutory and regulatory requirements."
    },
    {
        'filename': "MA.6032_CEO20241122_v20241101.pdf",
        'title': "Model of Care",
        'description': "This policy defines the process by which CalOptima Health develops, implements, manages, and evaluates the effectiveness of the Model of Care (MOC) for the OneCare Program. The policy outlines that CalOptima Health shall have a Member-centric MOC designed to ensure coordinated access to individualized quality health care and describes the components of the MOC."
    },
    {
        'filename': "MA.9002_CEO20250129_v20241231.pdf",
        'title': "Enrollee Grievance Process",
        'description': "This policy outlines the process by which CalOptima Health addresses and resolves enrollee grievances, including integrated grievances, related to Medi-Cal and Medicare covered services. It details the receipt, handling, and disposition of these grievances in accordance with applicable regulations and contractual requirements. The policy covers various aspects of enrollee dissatisfaction, such as quality of care, plan benefits, and difficulties contacting CalOptima Health."
    },
    {
        'filename': "MA.7007_CEO20241220_v20241201.pdf",
        'title': "Access and Availability",
        'description': "This policy establishes access and availability standards for members to obtain timely and appropriate care, including provider network adequacy. It describes the process CalOptima Health uses for monitoring network adequacy. The policy also addresses non-discrimination and flexibility in scheduling services for members with disabilities."
    },
    {
        'filename': "MA.6103_CEO20241122_v20241101.pdf",
        'title': "Pharmacy and Therapeutics\nCommittee and Formulary\nManagement",
        'description': "This policy defines Formulary Management for the OneCare program and outlines CalOptima Health’s Pharmacy and Therapeutics (P&T) Committee requirements. It details the requirements for P&T committee meetings, formulary adequacy, transition processes, and limitations on changes. The policy also outlines membership requirements for the P&T Committee, ensuring a diverse and qualified composition."
    },
    {
        'filename': "MA.2002_CEO20241122_v20241101.pdf",
        'title': "Marketing Activity Standards",
        'description': "This policy outlines the guidelines for Marketing Activities conducted by CalOptima Health OneCare Community Partners. It establishes marketing standards in accordance with federal regulations and defines what constitutes a marketing activity versus a communication activity. The policy also sets rules for marketing timelines and applies to all staff and partners involved in marketing on behalf of CalOptima Health."
    },
    {
        'filename': "MA.6009_CEO20240822_v20240801.pdf",
        'title': "Care Management and\nCoordination Process",
        'description': "This policy outlines the guidelines and processes for providing Care Management and Coordination to OneCare Members with multiple or complex conditions. CalOptima Health aims to maintain a Care Management program that helps members access care and services, coordinating their care through appropriate programs. The program includes identifying eligible members, offering services, and defining goals to improve functional capability in the right setting."
    },
    {
        'filename': "MA.9004_20250221.pdf",
        'title': "Expedited Pre-Service Integrated Appeal",
        'description': "This policy outlines the procedures for CalOptima Health to provide enrollees with an expedited process for appeals and integrated appeals related to pre-service organization determinations. It ensures compliance with CMS and DHCS requirements for Medi-Cal and Medicare covered services, addressing situations where standard appeal timelines could jeopardize an enrollee's health."
    },
    {
        'filename': "MA.6021_v20240101_CEO20240129_no attachments.pdf",
        'title': "Continuity of Care for Members\nInvoluntarily Transitioning\nBetween Providers or\nPractitioners",
        'description': "This policy outlines the process by which CalOptima Health ensures continuity of care for members involuntarily transitioning between providers or practitioners due to circumstances such as contract termination. It details the conditions under which CalOptima Health or a Health Network will consider approving the completion of covered services without interruption and includes an appeal process for continuity of care decisions."
    },
    {
        'filename': "MA.4004_CEO20241216_v20241201.pdf",
        'title': "Member Disenrollment",
        'description': "This policy outlines the procedures for disenrolling a member from the CalOptima Health OneCare program. It details both voluntary and involuntary disenrollment processes, including reasons for disenrollment and required actions by both the member and CalOptima Health. The policy also covers regulations regarding disenrollment surveys and record retention."
    },
    {
        'filename': "MA.6108_CEO20241216_v20241201.pdf",
        'title': "Medication Coordination of Benefits (COB)",
        'description': "This policy defines the criteria and process for Coordination of Benefits (COB) with other prescription drug coverage providers. It outlines how CalOptima Health will coordinate benefits with a Member’s Other Health Coverage (OHC), including conducting surveys, complying with CMS requirements, and establishing connectivity with CMS systems."
    },
    {
        'filename': "MA.7025_CEO20241010_v20241001.pdf",
        'title': "Primary Care Engagement and\nClinical Documentation\nIntegrity Program for\nCalOptima Health Community\nNetwork (CHCN) Contracted\nProviders",
        'description': "This policy outlines the Primary Care Engagement and Clinical Documentation Integrity Program for CalOptima Health Community Network (CHCN) contracted providers, specifically for the OneCare (OC) Program. The program aims to improve member engagement, clinical documentation accuracy, and completeness through incentivizing providers for reporting confirmed chronic conditions, managing these conditions, and reviewing preventive care needs during Annual Wellness Visits (AWV)."
    },
    {
        'filename': "MA.6107_CEO20241216_v20241201.pdf",
        'title': "Pharmacy Claims Processing",
        'description': "This policy outlines CalOptima Health's process for accurate and timely processing, payment, and reporting of pharmacy claims submitted by Contracted Network Pharmacies on behalf of OneCare Members. It details the responsibilities of CalOptima Health's Pharmacy Benefit Manager (PBM) in ensuring efficient and compliant claims adjudication."
    },
    {
        'filename': "MA.3003_CEO20240523.pdf",
        'title': "Medicare Shared Risk Pool",
        'description': "This policy outlines the process for CalOptima Health's administration of a Medicare Shared Risk Pool with a Shared Risk Group. It establishes the guidelines for setting the Medicare Shared Risk Budget, managing expenses, reporting, and reconciliation. The policy also details the process for surplus and deficit management within the pool."
    },
    {
        'filename': "MA.6112_CEO20241216_v20241201.pdf",
        'title': "Access to Part D Vaccines",
        'description': "This policy defines the process for providing covered Part D vaccines to CalOptima Health members. It outlines which vaccines are covered under Part D versus Part B of Medicare and specifies how members can access these vaccines through physicians and network pharmacies. The policy also covers reimbursement details, including administration costs and member co-payments."
    },
    {
        'filename': "MA.1004_CEO20241216_v20241201.pdf",
        'title': "Low Income Subsidy Cost-Sharing Data Corrections Based on Best Available Evidence",
        'description': "This policy defines the process for CalOptima Health to verify and correct a member's Low-Income Subsidy (LIS) Cost-Sharing status with the Centers for Medicare & Medicaid Services (CMS). It outlines the use of Best Available Evidence (BAE) to substantiate a member's LIS status and the procedures for initiating corrections or verifications with CMS based on documented evidence."
    },
    {
        'filename': "MA.6021a_CEO20240509_no attachments.pdf",
        'title': "Continuity of Care for New Members",
        'description': "This policy outlines CalOptima Health's process for ensuring continuity of care for newly enrolled members, particularly those with existing provider relationships or specific medical conditions like acute or chronic illnesses, pregnancy, or terminal illness. It aims to prevent delays or interruptions in medically necessary covered services by allowing members to continue seeing their existing providers under certain conditions, typically for a period of twelve months."
    },
    {
        'filename': "MA.6101_CEO20241122_v20241101.pdf",
        'title': "Medicare Part D Coverage Determination",
        'description': "This policy outlines CalOptima Health's process for making coverage determinations regarding drug benefits for Medicare Part D enrollees. It details what constitutes a coverage determination, who can request one, and the rights of members related to these determinations, including exceptions to the formulary and cost-sharing."
    },
    {
        'filename': "MA.6114_CEO20241122_v20241101.pdf",
        'title': "Medicare Part D\nRedeterminations",
        'description': "This policy outlines CalOptima Health's process for appealing drug benefit coverage and/or payment of drug benefits under Medicare Part D. It details the redetermination process, including who can request a redetermination, member rights, and timeframes for making a decision. The policy also covers acceptable formats for redetermination requests."
    },
    {
        'filename': "MA.1001_v20240101_CEO20240129_no attachments.pdf",
        'title': "OneCare Glossary of Terms",
        'description': "This policy defines terms used in CalOptima Health’s OneCare policies and procedures. It provides a glossary of definitions for various terms related to healthcare, member practices, and administrative processes within the OneCare program. The purpose is to ensure clarity and consistency in the application of OneCare policies."
    },
    {
        'filename': "MA.6105_CEO20241216_v20241201.pdf",
        'title': "Medication Quality Assurance",
        'description': "This policy establishes Quality Assurance (QA) measures and systems to reduce medication errors, minimize adverse drug interactions, and improve medication use. It outlines CalOptima Health's responsibilities in ensuring that Participating Pharmacies comply with minimum standards and in maintaining various DUR systems. The policy also emphasizes providing information to CMS and maintaining an electronic prescription drug program."
    },
    {
        'filename': "MA.4008_CEO20241216__v20241201.pdf",
        'title': "Member Handbook",
        'description': "This policy defines the required content and distribution procedures for the OneCare Member Handbook. It outlines the information CalOptima Health must provide to members regarding accessing the handbook, covered services, member procedures, financial obligations, prescription drug benefits, transportation services, advance directives, and grievance processes."
    },
    {
        'filename': "MA.4009_CEO20241010_v20241001.pdf",
        'title': "Member Orientation",
        'description': "This policy outlines the process for scheduling, conducting, evaluating, and revising Member orientations for the CalOptima Health OneCare program. It details how CalOptima Health provides these orientations to promote appropriate and timely access to covered services and improve member satisfaction. The policy covers various aspects such as language accessibility, individual orientations, and the content of the orientations."
    },
    {
        'filename': "MA.6110_CEO20241216_v20241201.pdf",
        'title': "Transition Process",
        'description': "This policy outlines CalOptima Health's transition process for Members to obtain a temporary supply of non-Formulary Part D drugs or Formulary drugs requiring Prior Authorization or Utilization Management restrictions. The policy aims to accommodate immediate needs and allow time to transition to Formulary alternatives or complete exceptions requests."
    },
    {
        'filename': "MA.6040_CEO20241122_v20241101.pdf",
        'title': "First Tier, Downstream, or\nRelated Entities (FDR) Model of\nCare – Roles and\nResponsibilities with Specific\nPersonal Care Coordinator\n(PCC) Requirements",
        'description': "This policy outlines the roles and responsibilities of Personal Care Coordinators (PCC) within the CalOptima Health OneCare program and contracted Health Networks. It aims to assist OneCare members in navigating the healthcare system and facilitate access to care, emphasizing care coordination and communication between stakeholders. The policy also details the goals of the comprehensive Model of Care (MOC) process, focusing on integrated care, data-driven approaches, and improved member outcomes."
    },
    {
        'filename': "MA.2012_CEO20241122_v20241101.pdf",
        'title': "Training and Oversight of\nCalOptima Health-Employed\nCommunity Partners",
        'description': "This policy outlines the training and oversight procedures for CalOptima Health Community Partners to ensure compliance with federal and state regulations, as well as CalOptima Health marketing policies. It details the requirements for training, monitoring, and performance reviews to maintain adherence to standards related to sales and marketing activities."
    },
    {
        'filename': "MA.6023_CEO20241220_20241201.pdf",
        'title': "Notice of Medicare Non-Coverage and\nNotice of a Detailed Explanation of\nNon-Coverage",
        'description': "This policy outlines the procedure for delivering the Notice of Medicare Non-Coverage (NOMNC) or Detailed Explanation of Non-Coverage (DENC) for Skilled Nursing Facilities (SNF), Home Health Agencies (HHA), or Comprehensive Outpatient Rehabilitation Facilities (CORF). It details responsibilities of SNFs, HHAs, and CORFs in delivering the NOMNC to members before covered services end and outlines when a Coverage Decision Letter should be issued instead."
    },

    # PA Folder
    {
        'filename': "PA.1000_CEO20240924_v20240901.pdf",
        'title': "CalOptima Health PACE Glossary of Terms",
        'description': "This policy defines terms used in CalOptima Health’s PACE (Programs of All-Inclusive Care for the Elderly) policies and procedures. It provides definitions for various financial and operational terms relevant to the PACE program, including service and non-service expenditures."
    },
    {
        'filename': "PA.1001_CEO20250306_v20250301.pdf",
        'title': "Equipment Maintenance and\nStorage",
        'description': "This policy outlines how the CalOptima Health PACE Center shall maintain all clinical Participant care equipment in accordance with manufacturers' recommendations. It details the preventive maintenance schedules, storage procedures, and reporting requirements for equipment-related incidents to ensure participant safety. The policy also assigns responsibilities for maintaining equipment records and ensuring code compliance."
    },
    {
        'filename': "PA.1002_CEO20240620_v20240601.pdf",
        'title': "Mandatory Medical Equipment and Supply Requirements",
        'description': "This policy defines the minimum standards for mandatory medical equipment and supplies that the CalOptima Health PACE Center must maintain. It outlines the quality, quantity, and maintenance regulations in accordance with the California Department of Health Care Services (DHCS) to ensure adequate care for participants."
    },
    {
        'filename': "PA.1003_20250221.pdf",
        'title': "PACE Center Space and\nPhysical Requirements",
        'description': "This policy outlines the construction and maintenance requirements for CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center day activity areas to ensure adherence to local, state, and federal regulations. It details specific requirements for the building, equipment, lighting, water supply, and other physical aspects of the PACE Center to maintain a safe and healthy environment for participants."
    },
    {
        'filename': "PA.1004_CEO20250306_v20250301.pdf",
        'title': "Maintenance and Housekeeping Standards",
        'description': "This policy outlines the procedures for maintenance and cleanliness at the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It ensures CalOptima Health PACE Centers are clean, safe, and in good repair for Participants and employees."
    },
    {
        'filename': "PA.1005_CEO20250306_v20250301.pdf",
        'title': "Collection, Storage, and\nRemoval of Waste",
        'description': "This policy outlines the requirements and procedures for CalOptima Health PACE Center employees to properly and safely remove and dispose of solid waste, biohazardous waste, and chemicals. It ensures compliance with regulations and maintains a clean environment within the PACE Center."
    },
    {
        'filename': "PA.2001_CEO20241031_v20250101_2025.pdf",
        'title': "Interdisciplinary Team (IDT) &\nParticipant Assessments",
        'description': "This policy outlines the components, purpose, and parameters of the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Interdisciplinary Team (IDT) and IDT meetings. The IDT is the core service delivery provider for PACE Participants and is responsible for the assessment, development, implementation, and evaluation of each Participant's treatment plan."
    },
    {
        'filename': "PA.2002_CEO20241031_v20250101_2025.pdf",
        'title': "Care Planning",
        'description': "This policy outlines how the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Interdisciplinary Team (IDT) will incorporate results of initial and subsequent assessments into a continuously updated Plan of Care for each Participant. It details the process of developing, evaluating, and revising a comprehensive person-centered Plan of Care, considering participant needs in all care domains. The policy also specifies timelines for initial plan development, semi-annual evaluations, and evaluations following changes in participant status."
    },
    {
        'filename': "PA.2003_CEO20250306_v20250101.pdf",
        'title': "PACE Palliative Care",
        'description': "This policy defines the scope and services of the Palliative Care Program for CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Participants. It outlines the requirements for providing palliative care services, including informing participants about the impact on their existing services and ensuring medically necessary care is provided. The policy also covers coordination of care, including advanced care planning and palliative care assessments."
    },
    {
        'filename': "PA.2005_v20240301_CEO20240307.pdf",
        'title': "Marketing and Outreach",
        'description': "This policy establishes guidelines for the development, distribution, and implementation of CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Marketing and Outreach Materials and activities. It outlines what constitutes marketing and outreach materials and activities, and specifies what is excluded from these categories."
    },
    {
        'filename': "PA.2010_CEO20240509.pdf",
        'title': "Enrollment and Intake",
        'description': "This policy outlines the enrollment and intake process for the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It details the stages involved, eligibility criteria, and responsibilities of different departments in determining an individual's suitability for the program."
    },
    {
        'filename': "PA.2020_v20240201_CEO20240212.pdf",
        'title': "Voluntary Disenrollment",
        'description': "This policy outlines the processes for a Participant’s voluntary disenrollment from the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It details the participant's right to disenroll at any time, the procedures CalOptima Health PACE will follow, and guidelines to ensure disenrollment decisions are made independently without coercion."
    },
    {
        'filename': "PA.2021_v20240201_CEO20240212.pdf",
        'title': "Involuntary Disenrollment",
        'description': "This policy outlines the processes for involuntary disenrollment of Participants from the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It details the circumstances under which CalOptima Health PACE can initiate such a disenrollment, emphasizing that all possible options to remedy a situation should be exhausted first and prior approval is required."
    },
    {
        'filename': "PA.2022_CEO20241031_v20250101_2025.pdf",
        'title': "Service Determination Request (SDR)",
        'description': "This policy outlines the procedures for identifying and processing Service Determination Requests (SDR) within the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It details how participants or their representatives can request services not included in their Plan of Care and the timelines for decision-making by the Interdisciplinary Team (IDT)."
    },
    {
        'filename': "PA.3001_CEO20250129_v20250101.pdf",
        'title': "Data Collection and Analysis",
        'description': "This policy defines the process by which CalOptima Health PACE provides consistent ongoing data collection and analysis concerning PACE Participants, their service utilization, and medical and social needs. CalOptima Health PACE shall translate data into information that can be used to identify opportunities for continuous quality improvement. The policy also outlines reporting requirements and compliance with data requirements from CMS and the State of California."
    },
    {
        'filename': "PA.5001_CEO20240509.pdf",
        'title': "Use of Physical and Chemical\nRestraints",
        'description': "This policy defines the appropriate use and termination of physical and chemical restraints by CalOptima Health PACE employees. It outlines the conditions under which restraints can be used, emphasizing the importance of minimizing their use and using the least restrictive methods possible. The policy also highlights the rights of participants to be free from harm, including restraints."
    },
    {
        'filename': "PA.5030_CEO20240509_no attachments.pdf",
        'title': "Wander Risk and Missing",
        'description': "This policy outlines the procedures for monitoring and searching for CalOptima Health PACE participants who are considered 'wander risks'. It aims to ensure the safety and wellbeing of these participants while they are at the PACE Center. The policy details identification methods, monitoring devices, and steps to take if a participant goes missing."
    },
    {
        'filename': "PA.5040_20250221.pdf",
        'title': "Participant Rights",
        'description': "This policy outlines the process for informing CalOptima Health PACE participants of their rights, ensuring understanding, and educating employees on adherence to these rights. It aims to promote participant rights and address any violations effectively. The policy emphasizes providing high-quality care that promotes autonomy and cooperation between participants, families, and CalOptima Health PACE providers."
    },
    {
        'filename': "PA.5042_v20240301_CEO20240320_no attachments.pdf",
        'title': "Safe Environment for\nParticipants at the PACE Center",
        'description': "This policy outlines the safety precautions and measures taken to provide a safe environment for participants at CalOptima Health PACE Centers. It covers topics such as facility design, safety audits, and compliance with reporting requirements for incidents involving participants' health and safety."
    },
    {
        'filename': "PA.5044_CEO20240509.pdf",
        'title': "Infection and Exposure Control Plan",
        'description': "This policy outlines how CalOptima Health PACE will minimize participant and employee exposure to infectious blood, bodily fluids, and airborne pathogens. It details the implementation of a PACE Infection Control Manual and Exposure Control Plan, adhering to Universal/Standard Precautions and CDC guidance."
    },
    {
        'filename': "PA.5050_v20240301_CEO20240320_no attachments.pdf",
        'title': "Nutrition",
        'description': "This policy outlines how CalOptima Health PACE provides nutritious meals to its participants and the oversight of the PACE Registered Dietician over the nutrition service. It details the responsibilities of the Registered Dietician including nutritional assessments, coordination of food services, and monitoring participant needs."
    },
    {
        'filename': "PA.5051_v20240301_CEO20240307_no attachments.pdf",
        'title': "Quality of Food",
        'description': "This policy outlines the standards for the quality of food served at the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It ensures that PACE Centers provide meal services that meet individual nutritional needs and are of high quality, serving nourishing, palatable, and well-balanced meals in a safe manner."
    },
    {
        'filename': "PA.5052_20250221.pdf",
        'title': "Utensil Cleaning Guidelines for\nNutritional Services",
        'description': "This policy outlines the procedure and guidelines for properly cleaning utensils used for nutritional services provided at the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It ensures utensils used to prepare and serve food to Participants are thoroughly disinfected after each use and that PACE Centers serve meals in a clean and safe environment."
    },
    {
        'filename': "PA.5053_20250221.pdf",
        'title': "Food Storage",
        'description': "This policy outlines guidelines for proper food storage of Participant food at CalOptima Health PACE Centers, ensuring a sanitary environment. It details requirements for food storage areas, temperature control, emergency supplies, and food safety audits. The policy applies to the PACE program."
    },
    {
        'filename': "PA.5054_20250221.pdf",
        'title': "Provision of Food Service and\nMenu Preparation",
        'description': "This policy outlines the guidelines and procedures for food service and menu preparation for Participants in the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It ensures that CalOptima Health PACE provides safe, nourishing, palatable, and well-balanced meals, including dietary counseling and education. The policy also addresses special dietary needs and preferences of the Participants."
    },
    {
        'filename': "PA.5110_CEO20240924_v20240901.pdf",
        'title': "Emergency Care",
        'description': "This policy outlines the process for CalOptima Health PACE employees to activate emergency services through the 911 system when a participant has an emergency medical condition. It covers emergency response protocols both inside and outside the CalOptima Health PACE Center, as well as requirements for employee training and participant emergency care plans."
    },
    {
        'filename': "PA.5111_CEO20240905_v20240901.pdf",
        'title': "After Hours Care",
        'description': "This policy outlines how CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) ensures that urgent and emergency care services are available to participants 24 hours a day, 7 days a week. It details the on-call coverage service and the procedures for handling participant calls after hours."
    },
    {
        'filename': "PA.5201_CEO20240822_v20240801.pdf",
        'title': "Medication Administration and\nPackaging",
        'description': "This policy outlines the procedures by which CalOptima Health PACE dispenses prescriptions to its participants, ensuring compliance with federal and state regulations. It details appropriate medication packaging methods, self-administration guidelines, and the handling of controlled substances, as well as prescription monitoring processes."
    },
    {
        'filename': "PA.5202_CEO20240620_v20240601.pdf",
        'title': "Labeling and Clinic Storage of Medications",
        'description': "This policy outlines the process for the labeling and storing of medications at the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It details the requirements for medication labeling by the contracted pharmacy and storage procedures within the CalOptima Health PACE clinic to ensure medication safety and accuracy for participants."
    },
    {
        'filename': "PA.5203_20250221.pdf",
        'title': "Return and Disposal of Medications",
        'description': "This policy outlines the standards and procedures for the proper return and disposal of medications by the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It includes guidelines for monthly medication reviews, identifying medications for disposal, and handling discontinued medications from participant supplies. The policy also addresses procedures for handling medication tampering and record retention."
    },
    {
        'filename': "PA.5204_CEO20240808_v20240801.pdf",
        'title': "Emergency Medication",
        'description': "This policy outlines the procedure for storing, maintaining, and administering emergency medications at the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) clinic. It details the requirements for the emergency medication supply, including its contents, storage, administration, and documentation."
    },
    {
        'filename': "PA.6001_20250221.pdf",
        'title': "Medical Records Maintenance",
        'description': "This policy defines the minimum standards for maintaining the Medical Record of a CalOptima Health Program for All-Inclusive Care for the Elderly (PACE) Participant. It outlines requirements for the organization, format, filing, storage, and release of medical records, ensuring compliance with HIPAA and other relevant regulations."
    },
    {
    'filename': "PA.7001_CEO20241216_v20250101_2025.pdf",
    'title': "Grievance Process",
    'description': "This policy outlines the grievance process for Participants in the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It ensures resolution of medical and non-medical grievances within thirty calendar days while maintaining confidentiality, adhering to regulatory and contractual requirements. CalOptima Health PACE is committed to addressing Participant concerns and dissatisfaction with services, care provision, or any aspect of the program."
    },
    {
        'filename': "PA.7002_CEO20241010_v20241001.pdf",
        'title': "Appeal Process",
        'description': "This policy outlines the appeal process for Participants in the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It ensures Participants, their representatives, or treating providers have the right to appeal decisions regarding care-related services or non-payment for services and that the process is handled respectfully and confidentially."
    },
    {
        'filename': "PA.7100_CEO20241205_v20241001.pdf",
        'title': "Premium and Share of Cost",
        'description': "This policy outlines the procedures for calculating and collecting premiums and share of cost for participants in the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE). It covers topics such as notifications of premium changes, payment due dates, and potential disenrollment for non-payment, as well as installment plan options."
    },
    {
        'filename': "PA.8001_v20240401_CEO20240417_no attachments.pdf",
        'title': "Reporting of Events Involving\nParticipant Health and Safety\nOccurring at the PACE Center",
        'description': "This policy outlines the procedures for notifying the Department of Health Care Services (DHCS) of reportable events involving Participants and their health and safety which occur at the CalOptima Health Program of All-Inclusive Care for the Elderly (PACE) Center. It details the reporting requirements and timelines for incidents such as death, injury, unusual occurrences, fires, and statistical summaries."
    },
    {
        'filename': "PA.9001_CEO20240620_v20240601.pdf",
        'title': "Medicare Part D Benefit\nInformation Tracking and\nReporting",
        'description': "This policy outlines the process for CalOptima Health PACE to track and report Participants' True Out-Of-Pocket (TrOOP) costs and Part D gross covered drug costs (GCDC) during enrollment and disenrollment, as required by CMS Part D regulations. It describes how TrOOP and GCDC are calculated, transferred between Part D plans, and reported to participants via a Transfer EOB document."
    },
    {
        'filename': "PA.9002_CEO20240620_v20240601.pdf",
        'title': "Pharmacy Claims Processing",
        'description': "This policy outlines the procedure for CalOptima Health PACE employees to ensure accurate and timely processing, payment, and reporting of claims submitted by Participating Pharmacies on behalf of Participants. It details the responsibilities of CalOptima Health PACE's Pharmacy Benefit Manager (PBM) in processing pharmacy claims."
    },
]