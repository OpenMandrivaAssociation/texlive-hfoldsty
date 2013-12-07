# revision 29349
# category Package
# catalog-ctan /fonts/hfoldsty
# catalog-date 2012-07-15 22:58:12 +0200
# catalog-license gpl
# catalog-version 1.15
Name:		texlive-hfoldsty
Version:	1.15
Release:	2
Summary:	Old style numerals with EC fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/hfoldsty
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfoldsty.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfoldsty.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfoldsty.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hfoldsty package provides virtual fonts for using oldstyle
(0123456789) figures with the European Computer Modern fonts.
It does a similar job as the eco package by Sebastian Kirsch
but includes a couple of improvements, i.e., better kerning
with guillemets, and support for character protruding using the
pdfcprot package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc3583.tfm
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc3583.vf
%{_texmfdistdir}/tex/latex/hfoldsty/hfoldsty.sty
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/omlhfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/omshfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfodh.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfoss.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfott.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfovt.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfoss.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfott.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfovtt.fd
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/Makefile
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/README
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/TODO
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/gpl.txt
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/hfoldsty.pdf
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/hfoldsty.xml
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/test-eco-hfo.tex
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/test-eco.tex
%doc %{_texmfdistdir}/doc/fonts/hfoldsty/test-hfo.tex
#- source
%doc %{_texmfdistdir}/source/fonts/hfoldsty/Makefile
%doc %{_texmfdistdir}/source/fonts/hfoldsty/hfoldsty.dtx
%doc %{_texmfdistdir}/source/fonts/hfoldsty/hfoldsty.ins
%doc %{_texmfdistdir}/source/fonts/hfoldsty/src/Makefile
%doc %{_texmfdistdir}/source/fonts/hfoldsty/src/TS1.etx
%doc %{_texmfdistdir}/source/fonts/hfoldsty/src/dostretch.mtx
%doc %{_texmfdistdir}/source/fonts/hfoldsty/src/generate.sh
%doc %{_texmfdistdir}/source/fonts/hfoldsty/src/t19.etx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
