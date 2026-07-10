%global tl_name captdef
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Declare free-standing \caption commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/captdef
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/captdef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/captdef.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The \DeclareCaption command defines a class of caption command
associated with the counter specified to the command. These commands are
free-standing (i.e., don't need to be inside a float environment). The
package uses \DeclareCaption to define \figcaption and \tabcaption,
which can be used outside figure or table environments.

