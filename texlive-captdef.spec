# revision 17353
# category Package
# catalog-ctan /macros/latex/contrib/captdef
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-captdef
Version:	20100309
Release:	1
Summary:	Declare free-standing \caption commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/captdef
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captdef.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captdef.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The \DeclareCaption command defines a class of caption command
associated with the counter specified to the command. These
commands are free-standing (i.e., don't need to be inside a
float environment). The package uses \DeclareCaption to define
\figcaption and \tabcaption, which can be used outside figure
or table environments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/captdef/captdef.sty
%doc %{_texmfdistdir}/doc/latex/captdef/captdef.pdf
%doc %{_texmfdistdir}/doc/latex/captdef/captdef.tex
%doc %{_texmfdistdir}/doc/latex/captdef/miscdoc.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
