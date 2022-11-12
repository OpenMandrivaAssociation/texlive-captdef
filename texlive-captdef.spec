Name:		texlive-captdef
Version:	17353
Release:	1
Summary:	Declare free-standing \caption commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/captdef
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captdef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captdef.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The \DeclareCaption command defines a class of caption command
associated with the counter specified to the command. These
commands are free-standing (i.e., don't need to be inside a
float environment). The package uses \DeclareCaption to define
\figcaption and \tabcaption, which can be used outside figure
or table environments.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/captdef/captdef.sty
%doc %{_texmfdistdir}/doc/latex/captdef/captdef.pdf
%doc %{_texmfdistdir}/doc/latex/captdef/captdef.tex
%doc %{_texmfdistdir}/doc/latex/captdef/miscdoc.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
