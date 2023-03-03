%global goipath github.com/cilium/cilium-cli
Version: 0.13.0

%gometa

Name: cilium-cli
Release: 1%{?dist}
Summary: CLI to install, manage & troubleshoot Kubernetes clusters running Cilium
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
LDFLAGS="-X github.com/cilium/cilium-cli/internal/cli/cmd.Version=%{version} "
%gobuild -o %{gobuilddir}/bin/cilium %{goipath}/cmd/cilium

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%{_bindir}/*

%changelog
* Wed Jan 11 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.13.0-1
- Bump to 0.13.0
* Wed Jan 11 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.12.12-1
- Bump to 0.12.12
* Sat Jan 07 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.12.11-1
- Initial build
