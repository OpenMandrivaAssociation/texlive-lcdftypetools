Name:		texlive-lcdftypetools
Version:	52851
Release:	2
Summary:	A bundle of outline font manipulation tools
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/lcdf-typetools
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcdftypetools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcdftypetools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-glyphlist
Requires:	texlive-lcdftypetools.bin

%description
This bundle of tools comprises: Cfftot1, which translates a
Compact Font Format (CFF) font, or a PostScript-flavored
OpenType font, into PostScript Type 1 format. It correctly
handles subroutines and hints; Mmafm and mmpfb, which create
instances of multiple-master fonts (mmafm and mmpfb were
previously distributed in their own package, mminstance);
Otfinfo, which reports information about OpenType fonts, such
as the features they support and the contents of their 'size'
optical size features; Otftotfm, which creates TeX font metrics
and encodings that correspond to a PostScript-flavored OpenType
font. It will interpret glyph positionings, substitutions, and
ligatures as far as it is able. You can say which OpenType
features should be activated; T1dotlessj, creates a Type 1 font
whose only character is a dotless j matching the input font's
design; T1lint, which checks a Type 1 font for correctness;
T1reencode, which replaces a font's internal encoding with one
you specify; and T1testpage, which creates a PostScript proof
for a Type 1 font. It is preliminary software.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/cfftot1.1*
%doc %{_texmfdistdir}/doc/man/man1/cfftot1.man1.pdf
%doc %{_mandir}/man1/mmafm.1*
%doc %{_texmfdistdir}/doc/man/man1/mmafm.man1.pdf
%doc %{_mandir}/man1/mmpfb.1*
%doc %{_texmfdistdir}/doc/man/man1/mmpfb.man1.pdf
%doc %{_mandir}/man1/otfinfo.1*
%doc %{_texmfdistdir}/doc/man/man1/otfinfo.man1.pdf
%doc %{_mandir}/man1/otftotfm.1*
%doc %{_texmfdistdir}/doc/man/man1/otftotfm.man1.pdf
%doc %{_mandir}/man1/t1dotlessj.1*
%doc %{_texmfdistdir}/doc/man/man1/t1dotlessj.man1.pdf
%doc %{_mandir}/man1/t1lint.1*
%doc %{_texmfdistdir}/doc/man/man1/t1lint.man1.pdf
%doc %{_mandir}/man1/t1rawafm.1*
%doc %{_texmfdistdir}/doc/man/man1/t1rawafm.man1.pdf
%doc %{_mandir}/man1/t1reencode.1*
%doc %{_texmfdistdir}/doc/man/man1/t1reencode.man1.pdf
%doc %{_mandir}/man1/t1testpage.1*
%doc %{_texmfdistdir}/doc/man/man1/t1testpage.man1.pdf
%doc %{_mandir}/man1/ttftotype42.1*
%doc %{_texmfdistdir}/doc/man/man1/ttftotype42.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
