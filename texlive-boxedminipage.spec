%global tl_name boxedminipage
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Framed minipages of a specified total width (text and frame combined)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/boxedminipage
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package essentially just wraps a minipage within an \fbox. However,
while \fbox{\begin{minipage}{\linewidth}...\end{minipage}} juts out into
the margin, \begin{boxedminipage}...\end{boxedminipage} does not.
Instead, it subtracts the frame's dimensions from the specified
dimensions of the minipage before typesetting the minipage. Note: The
package was formerly known as boxedminipage2e and now replaces Mario
Wolczko's earlier boxedminipage package.

