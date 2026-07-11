%global tl_name lcdftypetools
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A bundle of outline font manipulation tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/lcdf-typetools
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcdftypetools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcdftypetools.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(glyphlist)
Requires:	texlive(lcdftypetools.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle of tools comprises: Cfftot1, which translates a Compact Font
Format (CFF) font, or a PostScript-flavored OpenType font, into
PostScript Type 1 format. It correctly handles subroutines and hints;
Mmafm and mmpfb, which create instances of multiple-master fonts (mmafm
and mmpfb were previously distributed in their own package, mminstance);
Otfinfo, which reports information about OpenType fonts, such as the
features they support and the contents of their 'size' optical size
features; Otftotfm, which creates TeX font metrics and encodings that
correspond to a PostScript-flavored OpenType font. It will interpret
glyph positionings, substitutions, and ligatures as far as it is able.
You can say which OpenType features should be activated; T1dotlessj,
creates a Type 1 font whose only character is a dotless j matching the
input font's design; T1lint, which checks a Type 1 font for correctness;
T1reencode, which replaces a font's internal encoding with one you
specify; and T1testpage, which creates a PostScript proof for a Type 1
font. It is preliminary software.

